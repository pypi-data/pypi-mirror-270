import itertools
import json
import logging
import multiprocessing
import os
from functools import partial
from multiprocessing import Pool
from pathlib import Path
from typing import List, Union, Tuple, Optional, Type, Dict, Any
from typing import TYPE_CHECKING

import networkx as nx
import numpy as np
from networkx import connected_components
from tqdm.auto import tqdm

from . import config
from .file import RDYFile
from .osm import OSM
from .osm.utils import boxes_to_edges, iou
from .utils import GPSSeries, TimeSeries

if TYPE_CHECKING:
    from .widgets import Map

logger = logging.getLogger(__name__)


class Campaign:
    def __init__(self, name="",
                 folder: Union[list, str] = None,
                 recursive=True,
                 exclude: Union[list, str] = None,
                 sync_method: str = "timestamp",
                 timedelta_unit: str = 'timedelta64[ns]',
                 strip_timezone: bool = True,
                 trim_ends: bool = True,
                 lat_sw: float = None,
                 lon_sw: float = None,
                 lat_ne: float = None,
                 lon_ne: float = None,
                 download_osm_data: bool = False,
                 map_matching: bool = False,
                 osm_recurse_type: str = ">",
                 railway_types: Union[list, str] = None,
                 series: Union[List[Type[TimeSeries]], Type[TimeSeries]] = None):
        """

        Parameters
        ----------
        name: str
            Name of the campaign
        folder: Union[list, str]
            Folder or list of folders that should be imported
        recursive: bool, default: True
            Flag if folders should be searched recursively
        exclude: Union[list, str]
            Name(s) of file or folder that should be excluded
        sync_method: str
            Method to use to sync timestamps of individual files
        strip_timezone: bool, default: True
            Strips timezone from timestamps as np.datetime64 does not support timezones
        trim_ends: bool, default: True
            If True, cutoffs the measurements precisely to the timestamp when the measurement was started, respectively
            stopped. By default, Ridy measurement files can contain several seconds of measurements from before/after
            the button press
        lat_sw: float
            South west Latitude of the campaign, if the geographic extent is not given via arguments, the library tries
            to determine the geographic extent based on the GPS tracks
        lon_sw: float
            South west longitude of the campaign
        lat_ne: float
            North east latitude of the campaign
        lon_ne: float
            North east longitude of the campaign
        download_osm_data: bool, default: False
            If True download OSM data via the Overpass API
        map_matching: bool, default: False
            If True removes tries to match GPS track of each file to most reasonable OSM nodes
        railway_types: list or list of str
            Railway type to be downloaded from OSM, e.g., "rail", "subway", "tram" or "light_rail"
        osm_recurse_type : str
            Recurse type to be used when querying OSM data using the overpass API
        series: Union[List[Type[TimeSeries]], Type[TimeSeries]]
            Classes of TimeSeries to load, if None all TimeSeries of each file will be imported
        """
        self.folder = folder
        self.name = name
        self.files: List[RDYFile] = []
        self.grouped_files: Dict[Any, RDYFile] = {}

        # Geographic extent of campaign
        self.lat_sw, self.lon_sw = lat_sw, lon_sw
        self.lat_ne, self.lon_ne = lat_ne, lon_ne
        self.extent = [self.lon_sw, self.lat_sw, self.lon_ne, self.lat_ne]

        self.bboxs = []
        self.s_bboxs = []  # Simplified bounding boxes

        self.map_matching = map_matching

        self.osm = None
        self.osm_recurse_type = osm_recurse_type
        self.railway_types = railway_types
        self.osm_mappings = {}  # Map Matching results for each file

        # Sanity check if series is arg is valid
        if series:
            if type(series) is list:
                for s in series:
                    if not issubclass(s, TimeSeries):
                        raise ValueError("%s in %s is not a TimeSeries!" % (type(s), list(series)))
                self._series = series
            elif issubclass(series, TimeSeries):
                self._series = [series]
                pass
            else:
                raise ValueError("series argument must be list of TimeSeries or TimeSeries! not %s" % type(series))
        else:
            self._series = None

        if sync_method is not None and sync_method not in ["timestamp", "seconds", "device_time", "gps_time",
                                                           "ntp_time"]:
            raise ValueError(
                "synchronize argument must 'timestamp', 'seconds', 'device_time', 'gps_time' or 'ntp_time' not %s" %
                sync_method)

        self.sync_method = sync_method
        self.timedelta_unit = timedelta_unit # Only relevant for timestamp sync method
        self.strip_timezone = strip_timezone
        self.trim_ends = trim_ends

        self.results = {}  # Dictionary for Post Processing Results

        if folder:
            self.import_folder(self.folder, recursive, exclude,
                               trim_ends=self.trim_ends,
                               sync_method=self.sync_method,
                               timedelta_unit=self.timedelta_unit,
                               strip_timezone=self.strip_timezone)

        if not self.lat_sw or not self.lat_ne or not self.lon_sw or not self.lon_ne:
            self.determine_geographic_extent()

        if download_osm_data:
            self.download_osm_data()
        else:
            self.osm = None

    def __call__(self, name):
        results = list(filter(lambda file: file.filename == name, self.files))
        if len(results) == 1:
            return results[0]
        else:
            return results

    def __getitem__(self, index) -> RDYFile:
        return self.files[index]

    def __len__(self):
        return len(self.files)

    @property
    def osm(self):
        return self._osm

    @osm.setter
    def osm(self, value):
        for f in self:
            f.osm = value

        if self.map_matching:
            for f in tqdm(self, desc="Map Matching"):
                f.do_map_matching()

        self._osm = value

    def clear_files(self):
        """
            Clear all files from the campaign
        """
        self.files = []

    def create_map(self, center: Tuple[float, float] = None,
                   show_gps_tracks=True,
                   show_railway_elements=False) -> 'Map':
        """
        Creates a pyridy.widgets Map (based on ipyleaflet) showing the GPS tracks of measurement files

        Parameters
        ----------
        center: Tuple[float, float]
            The tuple containing the latitude/longitude of the marker.
        show_gps_tracks: bool
            Defines whether GPS tracks are shown or not
        show_railway_elements: bool
            Defines if railway elements are shown or not
        Returns
        -------
        Map : pyridy.widgets.Map
            Created map
        """
        from .widgets import Map

        if not center:
            center = self.determine_geographic_center()

        print(center)
        m = Map(center=center, zoom=12)

        # Plot OSM Tracks
        m.osm_routes_layer = m.add_osm_routes(self)

        # Plot measurement GPS Tracks
        if show_gps_tracks:
            m.measurement_layers = m.add_measurements(self)

        # Plot railway elements
        if show_railway_elements:
            m.railway_elements_layer = m.add_osm_railway_elements(self)

        return m

    def determine_geographic_extent(self):
        """
        Determines the geographic extent of the campaign in terms of min/max lat/lon

        Returns
        -------
        None
        """
        min_lats = []
        max_lats = []
        min_lons = []
        max_lons = []

        for f in self.files:
            gps_series = f.measurements[GPSSeries]
            if gps_series.is_empty():
                continue
            else:
                min_lats.append(gps_series.lat.min())
                max_lats.append(gps_series.lat.max())
                min_lons.append(gps_series.lon.min())
                max_lons.append(gps_series.lon.max())

        self.lat_sw = min(min_lats) if min_lats else None
        self.lat_ne = max(max_lats) if max_lats else None
        self.lon_sw = min(min_lons) if min_lons else None
        self.lon_ne = max(max_lons) if max_lons else None

        self.extent = [self.lon_sw, self.lat_sw, self.lon_ne, self.lat_ne]

        logging.info("Geographic boundaries of measurement campaign: Lat SW: %s, Lon SW: %s, Lat NE: %s, Lon NE: %s"
                     % (str(self.lat_sw), str(self.lon_sw), str(self.lat_ne), str(self.lon_ne)))

    def determine_geographic_center(self) -> Tuple[float, float]:
        """
        Determines the geographic center of the campaign.

        Returns
        -------
        Center : Tuple [float, float]
            Geographic center of the campaign

        Raises
        -------
        ValueError
            An error occurred determining the geographic center.
        """
        if self.lat_sw and self.lat_ne and self.lon_sw and self.lon_ne:
            return (
                (self.lat_sw + self.lat_ne) / 2,
                (self.lon_sw + self.lon_ne) / 2)
        else:
            raise ValueError("Cannot determine geographic center of campaign, enter manually using 'center' argument")

    def do_map_matching(self, rematch=False, **kwargs):
        """
        Performs map matching for all files in campaign

        Parameters
        ----------
        rematch: Bool, default: False
            If True performs map matching again, even when file already contains a map matching

        Returns
        -------
        None

        Raises
        -------
        RuntimeError
            An error occurred matching maps
        """
        if self.osm:
            for f in tqdm(self, desc="Map Matching: Files in Campaign"):
                if f.matched_ways and f.matched_nodes:
                    if rematch:
                        logger.info("(%s) File already has a map matching! Rematching..." % f.filename)
                        f.do_map_matching(**kwargs)
                    else:
                        logger.info("(%s) File already has a map matching! Skipping..." % f.filename)
                        continue
                else:
                    f.do_map_matching(**kwargs)
        else:
            raise RuntimeError("Can't do Map Matching, because no OSM data has been downloaded!")
        pass

    def group_by(self, key):
        """
        Group Ridy files by given key, grouped files can be accessed through the grouped_files attributes

        Parameters
        ----------
        key: Any
            Key that should be used to group files
        """
        f_sorted = sorted(self.files, key=key)
        self.grouped_files = {k: list(it) for k, it in itertools.groupby(f_sorted, key)}

    def determine_bounding_boxes(self, simplify=True, plot=False):
        """
        Determine bounding boxes of files and stores them in self.bboxs.

        Parameters
        ----------
        simplify: bool
            If True, unify bounding boxes with a large overlap to reduce number of queries and
            stores these in self.s_bboxs. Defaults to True.
        plot: bool
            Defaults to False.

        Returns
        -------
        None
        """
        self.bboxs = [f.bbox for f in self.files if f.bbox]
        if simplify:
            self.simplify_bounding_boxes()

    def simplify_bounding_boxes(self):
        """
        Unify bounding boxes with a large overlap to reduce number of queries. Cluster boxes by overlap

        Returns
        -------
        None
        """
        self.s_bboxs = []  # Filtered bounding boxes


        clusters = []
        for b1, b2 in itertools.combinations(self.bboxs, 2):
            if iou(b1, b2) > config.options["OSM_BOUNDING_BOX_SPLIT_IOU_THRES"]:
                clusters.append([str(b1), str(b2)])

        G = nx.Graph()
        for c in clusters:
            G.add_nodes_from(c)
            G.add_edges_from(boxes_to_edges(c))

        clusters = [list(c) for c in list(connected_components(G))]
        # Convert boxes back to float
        clusters = [[json.loads(b) for b in c] for c in clusters]

        # Add boxes not part of any cluster
        for b in self.bboxs:
            if b not in list(itertools.chain.from_iterable(clusters)):
                clusters.append([b])

        # Simplify boxes
        for c in clusters:
            arr = np.array(c)
            self.s_bboxs.append([arr[:, 0].min(), arr[:, 1].min(), arr[:, 2].max(), arr[:, 3].max()])

        # fig, ax = plt.subplots(1, figsize=(6, 6))
        # for b in self.bboxs:
        #     ax.add_patch(Rectangle((b[0], b[1]), b[2] - b[0], b[3] - b[1], alpha=1, edgecolor='r', facecolor='none'))
        #
        # for b in self.s_bboxs:
        #     ax.add_patch(Rectangle((b[0], b[1]), b[2] - b[0], b[3] - b[1], alpha=1, edgecolor='g', facecolor='none'))
        #
        # ax.grid()
        # ax.set_xlim([self.lon_sw, self.lon_ne])
        # ax.set_ylim([self.lat_sw, self.lat_ne])
        # plt.show()

    def download_osm_data(self, railway_types: Union[list, str] = None, osm_recurse_type: str = ">",):
        """
        Downloads the OSM data and

        Parameters
        ----------
        railway_types: Union[list, str]
            Railway type to be downloaded from OSM, e.g., "rail", "subway", "tram" or "light_rail". Defaults to None.
        osm_recurse_type: str
            Recurse type to be used when querying OSM data using the overpass API. Defaults to ">".

        Returns
        -------
        None
        """
        if railway_types:
            self.railway_types = railway_types

        if osm_recurse_type:
            self.osm_recurse_type = osm_recurse_type

        if config.options["OSM_SINGLE_BOUNDING_BOX"]:
            self.osm = OSM(bbox=self.extent, desired_railway_types=self.railway_types, recurse=self.osm_recurse_type)
        else:
            self.determine_bounding_boxes(simplify=False)
            if config.options["OSM_BOUNDING_BOX_OPTIMIZATION"]:
                self.simplify_bounding_boxes()
                self.osm = OSM(bbox=self.s_bboxs, desired_railway_types=self.railway_types,
                               recurse=self.osm_recurse_type)
            else:
                self.osm = OSM(bbox=self.bboxs, desired_railway_types=self.railway_types, recurse=self.osm_recurse_type)

    def import_files(self, file_paths: Union[list, str] = None,
                     sync_method: str = "timestamp",
                     timedelta_unit: str = 'timedelta64[ns]',
                     trim_ends: bool = True,
                     strip_timezone: bool = True,
                     det_geo_extent: bool = True,
                     use_multiprocessing: bool = False,
                     download_osm_data: bool = False,
                     railway_types: Union[list, str] = None,
                     osm_recurse_type: Optional[str] = None,
                     series: Union[List[Type[TimeSeries]], Type[TimeSeries]] = None):
        """ Import files into the campaign

        Parameters
        ----------
        file_paths: Union[list, str]
            Individual file paths of the files that should be imported
        sync_method: str
            Method to use for timestamp syncing
        timedelta_unit: str , default: 'timedelta64[ns]'
            Timedelta unit for timestamp sync method
        trim_ends: bool, default: True
            If True, trims measurement precisely to timestamp when the measurement was started respectively stopped
        strip_timezone: bool, default: True
            If True, strips timezone from timestamp arrays
        det_geo_extent: bool, default: True
            If True, determine the geographic extent of the imported files
        use_multiprocessing : bool, default: True
            If True, uses multiprocessing to import Ridy files
        download_osm_data: bool, default: False
            If True, download OSM Data via the Overpass API
        railway_types: str or list of str
            Railway types to be downloaded via the Overpass API
        osm_recurse_type : str
            Recurse type to be used when querying OSM data using the overpass API
        series: Union[List[Type[TimeSeries]], Type[TimeSeries]]
            Classes of TimeSeries to load, if None all TimeSeries of each file will be imported

        Raises
        -------
        TypeError
            Occurs if path's arguments are not of type str or list of str
        ValueError
            Error if the series is not of type Timeseries or if series' arguments ar not valid

        """
        if osm_recurse_type:
            self.osm_recurse_type = osm_recurse_type

        if railway_types:
            self.railway_types = railway_types

        if type(file_paths) == str:
            file_paths = [file_paths]
        elif type(file_paths) == list:
            pass
        else:
            raise TypeError("paths argument must be list of str or str")

        # Sanity check if series is arg is valid
        if series:
            if type(series) is list:
                for s in series:
                    if not issubclass(s, TimeSeries):
                        raise ValueError("%s in %s is not a TimeSeries!" % (type(s), list(series)))
                self._series = series
            elif issubclass(series, TimeSeries):
                self._series = [series]
                pass
            else:
                raise ValueError("series argument must be list of TimeSeries or TimeSeries! not %s" % type(series))

        if use_multiprocessing:
            with Pool(multiprocessing.cpu_count()) as p:
                files = list(tqdm(p.imap(partial(RDYFile,
                                                 sync_method=sync_method,
                                                 strip_timezone=strip_timezone,
                                                 trim_ends=trim_ends,
                                                 series=self._series), file_paths),
                                  desc="multiprocessing pool"))
                for f in files:
                    self.files.append(f)
        else:
            for p in tqdm(file_paths, desc="File Import"):
                self.files.append(RDYFile(path=p,
                                          sync_method=sync_method,
                                          timedelta_unit=timedelta_unit,
                                          strip_timezone=strip_timezone,
                                          trim_ends=trim_ends,
                                          series=self._series))

        if osm_recurse_type:
            self.osm_recurse_type = osm_recurse_type

        if det_geo_extent:
            self.determine_geographic_extent()

        if download_osm_data:
            self.download_osm_data()

    def import_folder(self, folder: Union[list, str] = None,
                      recursive: bool = True,
                      exclude: Union[list, str] = None,
                      **kwargs):
        """
        Imports folder(s) into the campaign

        Parameters
        ----------
        folder: str or list of str
            Folder(s) that should be imported
        recursive: bool, default: True
            Flag if folders should be imported recursively, i.e., whether subfolders should also be searched
        exclude: str or list of str
            Folder(s) or file(s) that should be excluded while importing

        Raises
        -------
        TypeError
            Occurs if folder's arguments are not of type str or list of str


        """
        if exclude is None:
            exclude = []
        elif type(exclude) == str:
            exclude = [exclude]

        if type(folder) == str:
            folder = [folder]
        elif type(folder) == list:
            pass
        else:
            raise TypeError("folder argument must be list or str")

        file_paths = []

        for fdr in folder:
            if recursive:
                all_paths = list(Path(fdr).rglob("*"))

                # File paths without excluded files or folder names
                for p in all_paths:
                    inter = set(p.parts).intersection(set(exclude))
                    if len(inter) > 0:
                        continue
                    else:
                        if p.suffix in [".rdy", ".sqlite"]:
                            file_paths.append(p)
                        else:
                            continue
            else:
                _, _, files = next(os.walk(fdr))
                for f in files:
                    file_path = os.path.join(fdr, f)
                    _, ext = os.path.splitext(file_path)
                    if f not in exclude and ext in [".rdy", ".sqlite"]:
                        file_paths.append(file_path)

                pass

        self.import_files(file_paths, **kwargs)
