import main

tflClient = main.tflAPI()


class stopPoint:
    """Stop Point from Unified API"""

    @staticmethod
    def getCategories():
        """Gets the list of available StopPoint additional information categories"""

        return tflClient.sendRequestUnified("/StopPoint/Meta/Categories", {})

    @staticmethod
    def getTypes():
        """Gets the list of available StopPoint types"""

        return tflClient.sendRequestUnified("/StopPoint/Meta/StopTypes", {})

    @staticmethod
    def getModes():
        """Gets the list of available StopPoint modes"""

        return tflClient.sendRequestUnified("/StopPoint/Meta/Modes", {})

    @staticmethod
    def getByIDs(ids, includeCrowdingData: bool):
        """
        Gets a list of StopPoints corresponding to the given list of stop ids

        :param ids: A list of stop point ids (station naptan code e.g. 940GZZLUASL).
        :param includeCrowdingData: Include the crowding data (static). To Filter further use: /StopPoint/{ids}/Crowding/{line}
        """

        return tflClient.sendRequestUnified(f"/StopPoint/{','.join(ids)}", {includeCrowdingData})

    @staticmethod
    def getAllByStopType(array):
        """
        Gets all stop points of a given type

        :param array: A list of valid stop types can be obtained from the StopPoint/meta/stoptypes endpoint
        """

        return tflClient.sendRequestUnified(f"/StopPoint/{tflClient.arrayToCSV(array)}", {})

    @staticmethod
    def getServiceTypesByID(stopPointID: str, lineIds, modes):
        """
        Gets the service types for a given Stop Point

        :param stopPointID:
        :param lineIds:
        :param modes:
        """

        return tflClient.sendRequestUnified(f"/StopPoint/ServiceTypes", {'id': stopPointID, 'lineIds': lineIds, 'modes': modes})

    @staticmethod
    def search(name: str, modes):
        """
        Search StopPoints by their common name. Will not return a valid NaPTAN for HUB

        :param name: Name of station
        :param modes: Eg. ['tfl', 'dlr']
        """

        return tflClient.sendRequestUnified(f"/StopPoint/Search/${name}", {'modes': tflClient.arrayToCSV(modes)})

    @staticmethod
    def getStationArrivals(naptanID: str):
        """
        Get all service arrivals

        :param naptanID: A StopPoint id (station naptan code e.g. 940GZZLUAS)
        """

        return tflClient.sendRequestUnified(f"StopPoint/${naptanID}/Arrivals", {})

    @staticmethod
    def getArrivalDepartures(naptanID: str, lineIds):
        """
        A StopPoint id (station naptan code e.g. 940GZZLUAS)

        :param naptanID: A StopPoint id (station naptan code e.g. 940GZZLUAS)
        :param lineIds: List of line ids e.g. ['tfl-rail', 'london-overground', 'thameslink']
        """

        return tflClient.sendRequestUnified(f"StopPoint/${naptanID}/ArrivalsDepartures", {lineIds})

    @staticmethod
    def getDisruptionsByID(ids, getFamily: bool, includeRouteBlockedStops: bool, flattenResponse: bool):
        """
        Gets all disruptions for the specified StopPointId, plus disruptions for any child Naptan records it may have

        :param ids: A list of StopPoint ids (station naptan code e.g. 940GZZLUAS)
        :param getFamily: Specify true to return disruptions for entire family, or false to return disruptions for just this stop point. Defaults to false.
        :param includeRouteBlockedStops:
        :param flattenResponse: Specify true to associate all disruptions with parent stop point. (Only applicable when getFamily is true)
        """

        return tflClient.sendRequestUnified(f"/StopPoint/{tflClient.arrayToCSV(ids)}/Disruption",
                                            {getFamily, includeRouteBlockedStops, flattenResponse})

    @staticmethod
    def getDisruptionsByMode(modes, includeRouteBlockedStops: bool):
        """
        Gets a distinct list of disrupted stop points for the given modes

        :param modes: An array of modes e.g. ['tube', 'dlr']
        :param includeRouteBlockedStops:
        """
        return tflClient.sendRequestUnified(f"/StopPoint/Mode/{tflClient.arrayToCSV(modes)}/Disruption",
                                            {includeRouteBlockedStops})

    @staticmethod
    def getReachableStationsByID(naptanID: str, lineID: str, serviceTypes=None):
        """
        Gets Stop points that are reachable from a station/line combination

        :param naptanID: A StopPoint id (station naptan code e.g. 940GZZLUAS)
        :param lineID: Line id of the line to filter by (e.g. victoria)
        :param serviceTypes: List of service types to filter on. Supported values: Regular, Night.
        """

        if serviceTypes is None:
            serviceTypes = ['Regular']
        return tflClient.sendRequestUnified(f"/StopPoint/{naptanID}/CanReachOnLine/{lineID}",
                                            {'serviceTypes': tflClient.arrayToCSV(serviceTypes)})

    @staticmethod
    def getRouteSectionByID(naptanID: str, serviceTypes):
        """
        Get the route sections for all the lines that service the given stop point id#

        :param naptanID: A StopPoint id (station naptan code e.g. 940GZZLUAS)
        :param serviceTypes: List of service types to filter on. Supported values: Regular, Night.
        """

        return tflClient.sendRequestUnified(f"/StopPoint/{naptanID}/Route",
                                            {'serviceTypes': tflClient.arrayToCSV(serviceTypes)})

    @staticmethod
    def getInRadius(stopTypes, radius: int, useStopPointHierarchy: bool, modes, categories, returnLines: bool,
                    latitude: int, longitude: int):
        """
        Gets a list of StopPoints within {radius} by the specified criteria

        :param stopTypes: A list of stopTypes that should be returned
        :param radius: The radius of the bounding circle in metres (default : 200)
        :param useStopPointHierarchy: Re-arrange the output into a parent/child hierarchy.
        :param modes: modes The list of modes to search eg. ['tube', 'dlr']
        :param categories: an optional list of comma separated property categories to return in the StopPoint's property bag. If null or empty, all categories of property are returned. Pass the keyword "none" to return no properties.Pass the keyword "none" to return no properties.
        :param returnLines: True to return the lines that each stop point serves as a nested resource.
        :param latitude:
        :param longitude:
        """

        return tflClient.sendRequestUnified(
            "/StopPoint",
            {
                'stopTypes': tflClient.arrayToCSV(stopTypes),
                'radius': radius,
                'useStopPointHierarchy': useStopPointHierarchy,
                'modes': tflClient.arrayToCSV(modes),
                'categories': tflClient.arrayToCSV(categories),
                'returnLines': returnLines,
                'latitude': latitude,
                'longitude': longitude
            }
        )

    @staticmethod
    def getBySMSCode(smsID: str, output: str):
        """
        Gets a StopPoint for a given sms code

        :param smsID: A 5-digit Countdown Bus Stop Code e.g. 73241, 50435, 56334.
        :param output: If set to "web", a 302 redirect to relevant website bus stop page is returned. All other values are ignored.
        """

        return tflClient.sendRequestUnified(f"/StopPoint/Sms/{smsID}", {output})

    @staticmethod
    def getTaxiRanksByID(naptanID: str):
        """
        Gets a list of taxi ranks corresponding to the given stop point id

        :param naptanID: A StopPoint id (station naptan code e.g. 940GZZLUAS)
        """

        return tflClient.sendRequestUnified(f"/StopPoint/{naptanID}/TaxiRanks", {})

    @staticmethod
    def getCarParksByID(naptanID: str):
        """
        Get car parks corresponding to the given stop point id

        :param naptanID: A StopPoint id (station naptan code e.g. 940GZZLUAS)
        """

        return tflClient.sendRequestUnified(f"/StopPoint/{naptanID}/CarParks", {})
