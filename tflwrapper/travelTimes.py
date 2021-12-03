from .tfl import tflAPI


class travelTimes(tflAPI):
    """Travel Times from Unified API"""

    def getOverlay(
        self,
        z,
        pinLat,
        pinLon,
        mapCenterLat,
        mapCenterLon,
        scenarioTitle,
        timeOfDayID,
        modeID,
        width,
        height,
        direction,
        travelTimeInterval
    ):
        """
        Gets the TravelTime overlay
        :param z: The zoom level
        :param pinLat: The latitude of the pin
        :param pinLon: The longitude of the pin
        :param mapCenterLat: The map center latitude
        :param mapCenterLon: The map center longitude
        :param scenarioTitle: The title of the scenario
        :param timeOfDayID: The id for the time of day (AM/INTER/PM)
        :param modeID: The id of the mode
        :param width: The width of the requested overlay
        :param height: The height of the requested overlay
        :param direction: The direction of travel
        :param travelTimeInterval:
        """
        return super(travelTimes, self).sendRequestUnified(
            f"/TravelTimes/overlay/{z}/mapcenter/{mapCenterLat}/{mapCenterLon}/pinlocation/{pinLat}/{pinLon}/dimensions/{width}/{height}/", {}
        )
