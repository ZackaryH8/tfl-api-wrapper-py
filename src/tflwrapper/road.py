from .tfl import tflAPI


class road(tflAPI):
    """Road from Unified API"""

    def getAll(self):
        """Get all roads managed by TfL"""

        return super(road, self).sendRequestUnified(
            '/Road', {}
        )

    def getByID(self, ids):
        """
        Get the road with the specified ID (Eg. A1)

        :param ids: ID(s) of the road(s). Eg. ['A1']
        """

        return super(road, self).sendRequestUnified(
            f'/Road/{self.arrayToCSV(ids)}', {}
        )

    def getStatusByID(self, ids, startDate, endDate):
        """
        Gets the specified roads with the status aggregated over the date range specified, or now until the end of today if no dates are passed.

        :param ids: ID(s) of the road(s). Eg. ['A1']
        :param startDate:
        :param endDate:
        """

        return super(road, self).sendRequestUnified(
            f'/Road/{self.arrayToCSV(ids)}', {'startDate': self.getRFC3339(startDate), 'endDate': self.getRFC3339(endDate)}
        )

    def getAllStreetDisruption(self, startDate, endDate):
        """
        Gets a list of disrupted streets

        @param startDate:
        @param endDate:
        """
        return super(road, self).sendRequestUnified(
            '/Road/all/Street/Disruption',
            {'startDate': self.getRFC3339(startDate), 'endDate': self.getRFC3339(endDate)}
        )

    def getAllDisruptionsByID(self, ids, stripContent: bool):
        """
        Gets a list of disrupted streets

        @param ids:
        @param stripContent: When true, removes every property/node except for id, point, severity, severityDescription,  startDate, endDate, corridor details, location and comments.
        """
        return super(road, self).sendRequestUnified(
            f'/Road/all/Disruption/{self.arrayToCSV(ids)}',
            {'stripContent': stripContent}
        )

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
