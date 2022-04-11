from .tfl import tflAPI


class disruptions(tflAPI):
    """Disruptions from Unified API"""

    def getAllLifts(self):
        """
        List of all currently disrupted lift routes, refreshed every 1 minute
        """
        return super(disruptions, self).sendRequestUnified(
            f"/Disruptions/Lifts"
        )
