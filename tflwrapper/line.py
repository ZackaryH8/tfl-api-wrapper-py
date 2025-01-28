from .tfl import tflAPI


class line(tflAPI):
    """Line from Unified API"""

    def getModes(self):
        """Gets a list of valid modes"""
        return super(line, self).sendRequestUnified(
            "/Line/Meta/Modes"
        )

    def getSeverityCodes(self):
        """Gets a list of valid severity codes"""
        return super(line, self).sendRequestUnified(
            "/Line/Meta/Severity"
        )

    def getDisruptionCategories(self):
        """Gets a list of valid disruption categories"""
        return super(line, self).sendRequestUnified(
            "/Line/Meta/DisruptionCatergories"
        )

    def getServiceTypes(self):
        """Gets a list of valid service types"""
        return super(line, self).sendRequestUnified(
            "/Line/Meta/ServiceTypes"
        )

    def getAllStopPoints(self, _line):
        """
        Gets a list of the stations that serve the given line id

        Args:
            line: The line id e.g. victoria, circle, N133        
        """
        return super(line, self).sendRequestUnified(
            F"/Line/{_line}/StopPoints"
        )
    

    def getAllByModes(self, modes):
        """
        Gets lines that serve the given modes
        
        Args:
            modes: A list of modes e.g. tube, tram
        """
        return super(line, self).sendRequestUnified(
            f"/Line/Mode/{self.arrayToCSV(modes)}"
        )

    def getStatusByLine(self, lines, detail = False, startDate = None, endDate = None):
        """
        Gets the line status of for given line ids e.g Minor Delays

        Args:
            lines: A list of line ids e.g. ['victoria', 'circle']
            detail: Include details of the disruptions that are causing the line status including the affected stops and routes
        """
        if startDate == None or endDate == None:
            return super(line, self).sendRequestUnified(
                f"/Line/{self.arrayToCSV(lines)}/Status", {'detail': detail }
            )
        else:
            return super(line, self).sendRequestUnified(
                f"/Line/{self.arrayToCSV(lines)}/Status/{self.getRFC3339(startDate)}/to/{self.getRFC3339(endDate)}", {'detail': detail }
            )

    def getStatusByModes(self, modes, detail = False, severityLevel = ""):
        """
        Gets the line status of for all lines for the given modes

        Args:
            modes: A list of modes e.g. tube, tram
            detail: Include details of the disruptions that are causing the line status including the affected stops and routes
            severityLevel: A list of severity codes to filter on. Supported values: Minor, Major, Severe
        """
        return super(line, self).sendRequestUnified(
            f"/Line/Mode/{self.arrayToCSV(modes)}/Status", {'detail': detail, 'severityLevel': severityLevel }
        )

    def getTimetableFromTo(self, _line, _from, _to):
        """
        Gets the timetable for a specified station on the give line with specified destination
        
        Args:
            _line: The line id e.g. victoria, circle, N133
            _from: The station id e.g. 940GZZLUASL
            _to: The destination station id e.g. 940GZZLUASL
        """
        return super(line, self).sendRequestUnified(
            f"/Line/{_line}/Timetable/{_from}/to/{_to}"
        )

    def getTimetableFromStation(self, _line, NaPTANID, direction):
        """
        Gets the inbound timetable for a specified station on the give line

        Args:
            _line: The line id e.g. victoria, circle, N133
            NaPTANID: The station id e.g. 940GZZLUASL
            direction: The direction of the timetable. Supported values: inbound, outbound. Defaulted to 'outbound' if not specified
        """
        return super(line, self).sendRequestUnified(
            f"/Line/{_line}/Timetable/{NaPTANID}",
            {'direction': direction}
        )

    def getArrivalsByNaptan(self, lineids, naptan, destinationStationId, direction = "all"):
        """
        Gets the arrivals for a given station on the give line

        Args:
            lineids: A list of line ids e.g. ['victoria', 'circle']
            naptan: The station id e.g. 940GZZLUASL
            destinationStationId: The destination station id e.g. 940GZZLUASL
            direction: The direction of the timetable. Supported values: inbound, outbound. Defaulted to 'all' if not specified
        """
        return super(line, self).sendRequestUnified(
            f"/Line/{self.arrayToCSV(lineids)}/Arrivals/{naptan}", {'direction': direction, 'destinationStationId': destinationStationId }
        )

    def getAllValidRoutes(self, serviceTypes):
        """
        Get all valid routes for all lines, including the name and id of the originating and terminating stops for each route.

        Args:
            serviceTypes: A list of service types e.g. 'tube, 'tram'. Supported values: Regular, Night. Defaulted to 'Regular' if not specified
        """
        return super(line, self).sendRequestUnified(
            f"/Line/Route", {
                'serviceTypes': serviceTypes}
        )

    def getStatusByID(self, lineids, detail: bool):
        """
        Gets the line status of for all lines for the given modes

        Args:
            lineids: A list of line ids e.g. ['victoria', 'circle']
            detail: Include details of the disruptions that are causing the line status including the affected stops and routes
        """
        return super(line, self).sendRequestUnified(
            f"/Line/Mode/{self.arrayToCSV(lineids)}/Status", {'detail': detail}
        )

    def getRouteByIDs(self, lineids, serviceTypes):
        """
        Get all valid routes for given line ids, including the name and id of the originating and terminating stops for each route
        Args:
            lineids: A list of line ids e.g. ['victoria', 'circle']
            serviceTypes: A list of service types e.g. 'tube, 'tram'. Supported values: Regular, Night. Defaulted to 'Regular' if not specified
        """
        return super(line, self).sendRequestUnified(
            f"/Line/{self.arrayToCSV(lineids)}/Route", {
                'serviceTypes': serviceTypes}
        )
