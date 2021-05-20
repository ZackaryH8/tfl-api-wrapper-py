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

    def getStatusByID(self, lineIDs, detail: bool):
        """
        Gets the line status of for all lines for the given modes

        :param lineIDs: A comma-separated list of line ids e.g. ['victoria', 'circle']
        :param detail: Include details of the disruptions that are causing the line status including the affected stops and routes
        """
        return super(line, self).sendRequestUnified(
            f"/Line/Mode/{self.arrayToCSV(lineIDs)}/Status", {'detail': detail}
        )

    def getRouteByIDs(self, lineIDs, serviceTypes):
        """
        Get all valid routes for given line ids, including the name and id of the originating and terminating stops for each route.

        :param lineIDs: A list of line ids e.g. ['victoria', 'circle']
        :param detail: A list of service types to filter on. Supported values: Regular, Night. Defaulted to 'Regular' if not specified
        """
        return super(line, self).sendRequestUnified(
            f"/Line/{self.arrayToCSV(lineIDs)}/Route", {
                'serviceTypes': serviceTypes}
        )
