from .tfl import tflAPI


class airQuality(tflAPI):
    """Air Quality from the TFL Unified API"""

    def getAirQuality(self):
        """
        Get all current and future air quality forecast
        """
        return super(airQuality, self).sendRequestUnified(
            f"/AirQuality", {}
        )
