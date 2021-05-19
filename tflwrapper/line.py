from .tfl import tflAPI


class line(tflAPI):
    """Bike point from Unified API"""

    def getModes(self):
        """Gets a list of valid modes"""
        return super(line, self).sendRequestUnified(
            "/Line/Meta/Modes", {}
        )

    def getSeverityCodes(self):
        """Gets a list of valid severity codes"""
        return super(line, self).sendRequestUnified(
            "/Line/Meta/Severity", {}
        )

    def getDisruptionCategories(self):
        """Gets a list of valid disruption categories"""
        return super(line, self).sendRequestUnified(
            "/Line/Meta/DisruptionCatergories", {}
        )

    def getServiceTypes(self):
        """Gets a list of valid service types"""
        return super(line, self).sendRequestUnified(
            "/Line/Meta/ServiceTypes", {}
        )

    def getAllFromMode(self, modes):
        """Gets lines that serve the given modes"""
        return super(line, self).sendRequestUnified(
            f"/Line/Mode/{self.arrayToCSV(modes)}", {}
        )

    def getStatusByModes(self, modes):
        """Gets the line status of for all lines for the given modes"""
        return super(line, self).sendRequestUnified(
            f"/Line/Mode/{self.arrayToCSV(modes)}/Status", {}
        )
