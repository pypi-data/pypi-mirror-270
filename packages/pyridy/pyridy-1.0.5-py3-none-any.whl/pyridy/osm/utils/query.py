import overpy


class QueryResult:
    def __init__(self, result: overpy.Result, railway_type: str):
        """
        Class representing the Query Result

        Parameters
        ----------
        result: overpy.Result
            Result of the overpy query
        railway_type: str
            Railway type that was used for this query

        Returns
        -------
        None
        """
        self.railway_type = railway_type
        self.result: overpy.Result = result

    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value: overpy.Result):
        """
        Assigns ways to nodes

        Parameters
        ----------
        value : overpy.Result
            The result whose nodes are assigned ways to

        Returns
        -------
        None
        """
        if value:
            for way in value.ways:
                for node in way.nodes:
                    if hasattr(node, "ways"):
                        node.ways.append(way)
                    else:
                        node.ways = [way]

        self._result = value
