from .tfl import tflAPI


class road(tflAPI):
    """Road from Unified API"""

    def getCategories(self):
        """Gets a list of valid RoadDisruption categories"""
        
        return super(road, self).sendRequestUnified(
            '/Road/Meta/Categories',
            {}
        )

    def getSeverities(self):
        """Gets a list of valid RoadDisruption severity codes"""

        return super(road, self).sendRequestUnified(
            '/Road/Meta/Severities',
            {}
        )

    def getAll(self):
        """Get all roads managed by TfL"""

        return super(road, self).sendRequestUnified(
            '/Road'
        )

    def getByID(self, ids):
        """
        Get the road with the specified ID (Eg. A1)
        Args:
            ids: ID(s) of the road(s). Eg. ['A1']
        """

        return super(road, self).sendRequestUnified(
            f'/Road/{self.arrayToCSV(ids)}'
        )

    def getStatusByID(self, ids, startDate, endDate):
        """
        Gets the specified roads with the status aggregated over the date range specified, or now until the end of today if no dates are passed.
        Args:
            ids: ID(s) of the road(s). Eg. ['A1']
            startDate: Optional, the start time to filter on
            endDate: Optional, the end time to filter on
        """

        return super(road, self).sendRequestUnified(
            f'/Road/{self.arrayToCSV(ids)}', {'startDate': self.getRFC3339(
                startDate), 'endDate': self.getRFC3339(endDate)}
        )

    def getAllStreetDisruption(self, startDate, endDate):
        """
        Gets a list of disrupted streets

        Args:
            startDate: Optional, the start time to filter on
            endDate: Optional, the end time to filter on
        """
        return super(road, self).sendRequestUnified(
            '/Road/all/Street/Disruption',
            {'startDate': self.getRFC3339(
                startDate), 'endDate': self.getRFC3339(endDate)}
        )

    def getAllDisruptionsByID(self, ids, stripContent: bool = False):
        """
        Gets a list of disrupted streets

        Args:
            ids: ID(s) of the road(s). Eg. ['A1']
            stripContent: Optional, if true, the content of the disruption will be stripped from the response
        """
        return super(road, self).sendRequestUnified(
            f'/Road/all/Disruption/{self.arrayToCSV(ids)}',
            {'stripContent': stripContent}
        )
