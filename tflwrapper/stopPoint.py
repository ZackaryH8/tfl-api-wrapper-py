from .tfl import tflAPI


class stopPoint(tflAPI):
    """Stop Point from Unified API"""

    def getCategories(self):
        """Gets the list of available StopPoint additional information categories"""
        return super(stopPoint, self).sendRequestUnified(
            "/StopPoint/Meta/Categories"
        )

    def getTypes(self):
        """Gets the list of available StopPoint types"""

        return super(stopPoint, self).sendRequestUnified(
            "/StopPoint/Meta/StopTypes"
        )

    def getModes(self):
        """Gets the list of available StopPoint modes"""

        return super(stopPoint, self).sendRequestUnified(
            "/StopPoint/Meta/Modes"
        )

    def getByIDs(self, ids, includeCrowdingData: bool):
        """
        Gets a list of StopPoints corresponding to the given list of stop ids

        Args:
            ids: A list of StopPoint ids (station naptan code e.g. 940GZZLUAS)
            includeCrowdingData: Specify true to return crowding data (static) for each stop point
        """

        return super(stopPoint, self).sendRequestUnified(
            f"/StopPoint/{','.join(ids)}", {'includeCrowdingData': includeCrowdingData}
        )

    def getAllByStopType(self, array):
        """
        Gets all stop points of a given type

        Args:
            array: An array of stop point types e.g. ['NaptanPublicBusCoachTram']
        """

        return super(stopPoint, self).sendRequestUnified(
            f"/StopPoint/{super(stopPoint, self).arrayToCSV(array)}"
        )

    def getServiceTypesByID(self, stopPointID: str, lineIds, modes):
        """
        Gets the service types for a given Stop Point

        Args:
            stopPointID: A StopPoint id (station naptan code e.g. 940GZZLUAS)
            lineIds: A list of Line ids (e.g. victoria)
            modes: An array of modes e.g. ['tube', 'dlr']
        """

        return super(stopPoint, self).sendRequestUnified(
            f"/StopPoint/ServiceTypes",
            {"id": stopPointID, "lineIds": lineIds, "modes": modes},
        )

    def search(self, name: str, modes):
        """
        Search StopPoints by their common name. Will not return a valid NaPTAN for HUB

        Args:
            name: The name of station to search for
            modes: An array of modes e.g. ['tube', 'dlr']
        """

        return super(stopPoint, self).sendRequestUnified(
            f"/StopPoint/Search/${name}",
            {"modes": super(stopPoint, self).arrayToCSV(modes)},
        )

    def getStationArrivals(self, naptanID: str):
        """
        Get all service arrivals

        Args:
            naptanID: A StopPoint id (station naptan code e.g. 940GZZLUAS)
        """

        return super(stopPoint, self).sendRequestUnified(
            f"/StopPoint/{naptanID}/Arrivals"
        )

    # def getArrivalsDepartures(self, naptanID: str, lineIds):
    #     """
    #     Get all service arrivals and departures

    #     :param naptanID: A StopPoint id (station naptan code e.g. 940GZZLUAS)
    #     :param lineIds: List of line ids e.g. ['tflwrapper-rail', 'london-overground', 'thameslink']
    #     """

    #     return super(stopPoint, self).sendRequestUnified(
    #         f"StopPoint/${naptanID}/ArrivalsDepartures", {'lineIds': lineIds}
    #     )

    def getDisruptionsByID(
        self,
        ids,
        getFamily: bool,
        includeRouteBlockedStops: bool,
        flattenResponse: bool,
    ):
        """
        Gets all disruptions for the specified StopPointId, plus disruptions for any child Naptan records it may have

        Args:
            ids: A list of StopPoint ids (station naptan code e.g. 940GZZLUAS)
            getFamily: Specify true to return disruptions for entire family, or false to return disruptions for just this stop point. Defaults to false.
            includeRouteBlockedStops: Specify true to return disruptions for route blocked stops, or false to return disruptions for all stops. Defaults to false.
            flattenResponse: Specify true to return a flattened response, or false to return a nested response. Defaults to false.
        """

        return super(stopPoint, self).sendRequestUnified(
            f"/StopPoint/{super(stopPoint, self).arrayToCSV(ids)}/Disruption",
            {'getFamily': getFamily, 'includeRouteBlockedStops': includeRouteBlockedStops, 'flattenResponse': flattenResponse},
        )

    def getDisruptionsByMode(self, modes, includeRouteBlockedStops: bool):
        """
        Gets a distinct list of disrupted stop points for the given modes

        Args:
            modes: An array of modes e.g. ['tube', 'dlr']
            includeRouteBlockedStops: Specify true to return disruptions for route blocked stops, or false to return disruptions for all stops. Defaults to false.
        """
        return super(stopPoint, self).sendRequestUnified(
            f"/StopPoint/Mode/{super(stopPoint, self).arrayToCSV(modes)}/Disruption",
            {'includeRouteBlockedStops': includeRouteBlockedStops},
        )

    def getReachableStationsByID(self, naptanID: str, lineID: str, serviceTypes=None):
        """
        Gets Stop points that are reachable from a station/line combination

        Args:
            naptanID: A StopPoint id (station naptan code e.g. 940GZZLUAS)
            lineID: A Line id (e.g. victoria)
            serviceTypes: An array of service types. Supported values: Regular, Night. Defaults to Regular.
        """

        if serviceTypes is None:
            serviceTypes = ["Regular"]
        return super(stopPoint, self).sendRequestUnified(
            f"/StopPoint/{naptanID}/CanReachOnLine/{lineID}",
            {"serviceTypes": super(stopPoint, self).arrayToCSV(serviceTypes)},
        )

    def getRouteSectionByID(self, naptanID: str, serviceTypes):
        """
        Get the route sections for all the lines that service the given stop point id#

        Args:
            naptanID: A StopPoint id (station naptan code e.g. 940GZZLUAS)
            serviceTypes: An array of service types. Supported values: Regular, Night.
        """

        return super(stopPoint, self).sendRequestUnified(
            f"/StopPoint/{naptanID}/Route",
            {"serviceTypes": super(stopPoint, self).arrayToCSV(serviceTypes)},
        )

    def getInRadius(
        self,
        stopTypes,
        radius: int,
        useStopPointHierarchy: bool,
        modes,
        categories,
        returnLines: bool,
        latitude: int,
        longitude: int,
    ):
        """
        Gets a list of StopPoints within {radius} by the specified criteria

        Args:
            stopTypes: An array of stop point types e.g. ['NaptanPublicBusCoachTram']
            radius: The radius in metres. Defaults to 200.
            useStopPointHierarchy: Specify true to return stop points in the hierarchy, or false to return stop points at the specified radius. Defaults to false.
            modes: An array of modes e.g. ['tube', 'dlr']
            categories: An array of categories e.g. ['tram', 'bus']
            returnLines: Specify true to return the lines that service the stop point, or false to return the stop point itself. Defaults to false.
            latitude: The latitude of the location to search from.
            longitude: The longitude of the location to search from.
        """

        return super(stopPoint, self).sendRequestUnified(
            "/StopPoint",
            {
                "stopTypes": super(stopPoint, self).arrayToCSV(stopTypes),
                "radius": radius,
                "useStopPointHierarchy": useStopPointHierarchy,
                "modes": super(stopPoint, self).arrayToCSV(modes),
                "categories": super(stopPoint, self).arrayToCSV(categories),
                "returnLines": returnLines,
                "latitude": latitude,
                "longitude": longitude,
            },
        )

    def getBySMSCode(self, smsID: str, output: str):
        """
        Gets a StopPoint for a given sms code
        
        Args:
            smsID: A 5-digit sms code e.g. 73241, 50435, 5633.
            output: If set to "web", a 302 redirect to relevant website bus stop page is returned. All other values are ignored.
        """

        return super(stopPoint, self).sendRequestUnified(
            f"/StopPoint/Sms/{smsID}", {'output': output}
        )

    def getTaxiRanksByID(self, naptanID: str):
        """
        Gets a list of taxi ranks corresponding to the given stop point id

        Args:
            naptanID: A StopPoint id (station naptan code e.g. 940GZZLUAS)
        """

        return super(stopPoint, self).sendRequestUnified(
            f"/StopPoint/{naptanID}/TaxiRanks"
        )

    def getCarParksByID(self, naptanID: str):
        """
        Get car parks corresponding to the given stop point id

        Args:
            naptanID: A StopPoint id (station naptan code e.g. 940GZZLUAS)
        """

        return super(stopPoint, self).sendRequestUnified(
            f"/StopPoint/{naptanID}/CarParks"
        )
