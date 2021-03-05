from .tfl import tflAPI


class trackerNet(tflAPI):
    """TrackerNet API"""

    def getPredictionSummary(self, line: str):
        """Get detailed train prediction information for a nominated station on a nominated line within 100 minute range"""

        return super(trackerNet, self).sendRequestTrackerNet(
            f"/PredictionSummary/${line}"
        )

    def getPredictionDetailed(self, line: str, stationCode: str):
        """Get detailed train prediction information for a nominated station on a nominated line within 100 minute range"""

        return super(trackerNet, self).sendRequestTrackerNet(
            f"/PredictionDetailed/{line}/{stationCode}"
        )

    def getAllLinesStatus(self, incidentsOnly: bool):
        """
        Get the status of all lines on the network indicating any delays, disruptions or suspensions on the lines.

        :param incidentsOnly: Get station status information for stations with incidents only
        """

        incidentsOnlyCheck = '/IncidentsOnly' if incidentsOnly else ''
        return super(trackerNet, self).sendRequestTrackerNet(
            f"/LineStatus{incidentsOnlyCheck}"
        )

    def getAllStationStatus(self, incidentsOnly: bool):
        """
        Get station status information for all stations

        :param incidentsOnly: Get station status information for stations with incidents only
        """

        incidentsOnlyCheck = '/IncidentsOnly' if incidentsOnly else ''
        return super(trackerNet, self).sendRequestTrackerNet(
            f"/StationStatus{incidentsOnlyCheck}"
        )