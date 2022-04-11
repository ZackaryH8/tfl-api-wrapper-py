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

        Args:
            z: The zoom level of the map
            pinLat: The latitude of the pin
            pinLon: The longitude of the pin
            mapCenterLat: The latitude of the map center
            mapCenterLon: The longitude of the map center
            scenarioTitle: The title of the scenario
            timeOfDayID: The time of day ID. Supported values: AM, INTER, PM
            modeID: The mode ID.
            width: The width of the map
            height: The height of the map
            direction: The direction of the travel
            travelTimeInterval: The travel time interval
        """
        return super(travelTimes, self).sendRequestUnified(
            f"/TravelTimes/overlay/{z}/mapcenter/{mapCenterLat}/{mapCenterLon}/pinlocation/{pinLat}/{pinLon}/dimensions/{width}/{height}/", {}
        )
