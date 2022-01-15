from .tfl import tflAPI


class line(tflAPI):
    """Line from Unified API"""

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

    def getAllStopPoints(self, line):
        """
        Gets a list of the stations that serve the given line id
        :param line: A line id e.g. victoria, circle, N133
        """
        return super(line, self).sendRequestUnified(
            F"/Line/{line}/StopPoints", {}
        )
    

    def getAllByModes(self, modes):
        """
        Gets lines that serve the given modes
        :param modes: An list of modes e.g. tube, tram
        """
        return super(line, self).sendRequestUnified(
            f"/Line/Mode/{self.arrayToCSV(modes)}", {}
        )

    def getStatusByLine(self, lines, detail = False, startDate = None, endDate = None):
        """
        Gets the line status of for given line ids e.g Minor Delays

        :param lines: A list of line ids e.g. victoria, circle, N133
        :param detail: Include details of the disruptions that are causing the line status including the affected stops and routes
        """
        if startDate == None or endDate == None:
            return super(line, self).sendRequestUnified(
                f"/Line/{self.arrayToCSV(lines)}/Status", { detail }
            )
        else:
            return super(line, self).sendRequestUnified(
                f"/Line/{self.arrayToCSV(lines)}/Status/{self.getRFC3339(startDate)}/to/{self.getRFC3339(endDate)}", { detail }
            )

    def getStatusByModes(self, modes, detail = False, severityLevel = ""):
        """
        Gets the line status of for all lines for the given modes

        :param modes: An list of modes e.g. tube, tram
        :param detail: Include details of the disruptions that are causing the line status including the affected stops and routes
        :param severityLevel: If specified, ensures that only those line status(es) are returned within the lines that have disruptions with the matching severity level
        """
        return super(line, self).sendRequestUnified(
            f"/Line/Mode/{self.arrayToCSV(modes)}/Status", { detail, severityLevel }
        )

    def getTimetableFromTo(self, _line, _from, _to):
        """Gets the timetable for a specified station on the give line with specified destination"""
        return super(line, self).sendRequestUnified(
            f"/Line/{_line}/Timetable/{_from}/to/{_to}"
        )

    def getTimetableFromStation(self, _line, NaPTANID, direction):
        """
        Gets the inbound timetable for a specified station on the give line

        :param _line: Id of the line e.g. 'victoria'
        :param NaPTANID: Id of the stop (station naptan code e.g. 940GZZLUASL)
        :param direction: Leave blank for outbound or "inbound"
        """
        return super(line, self).sendRequestUnified(
            f"/Line/{_line}/Timetable/{NaPTANID}",
            {'direction': direction}
        )

    def getArrivalsByNaptan(self, lineids, naptan, destinationStationId, direction = "all"):
        """
        """
        return super(line, self).sendRequestUnified(
            f"/Line/{self.arrayToCSV(lineids)}/Arrivals/{naptan}", {'direction': direction, 'destinationStationId': destinationStationId }
        )

    def getAllValidRoutes(self, serviceTypes):
        """
        Get all valid routes for all lines, including the name and id of the originating and terminating stops for each route.

        :param serviceTypes:A comma seperated list of service types to filter on. Supported values: Regular, Night. Defaulted to 'Regular' if not specified
        """
        return super(line, self).sendRequestUnified(
            f"/Line/Route", {
                'serviceTypes': serviceTypes}
        )

    def getStatusByID(self, lineids, detail: bool):
        """
        Gets the line status of for all lines for the given modes

        :param lineids: A comma-separated list of line ids e.g. ['victoria', 'circle']
        :param detail: Include details of the disruptions that are causing the line status including the affected stops and routes
        """
        return super(line, self).sendRequestUnified(
            f"/Line/Mode/{self.arrayToCSV(lineids)}/Status", {'detail': detail}
        )

    def getRouteByIDs(self, lineids, serviceTypes):
        """
        Get all valid routes for given line ids, including the name and id of the originating and terminating stops for each route

        :param lineids: A list of line ids e.g. ['victoria', 'circle']
        :param detail: A list of service types to filter on. Supported values: Regular, Night. Defaulted to 'Regular' if not specified
        """
        return super(line, self).sendRequestUnified(
            f"/Line/{self.arrayToCSV(lineids)}/Route", {
                'serviceTypes': serviceTypes}
        )
