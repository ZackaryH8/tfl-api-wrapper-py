from .tfl import tflAPI


class mode(tflAPI):
    """Mode API, /mode"""

    def getActiveServiceTypes(self):
        """Returns the service type active for a mode, currently only supports tube"""

        return super(mode, self).sendRequestUnified(
            "/Mode/ActiveServiceTypes", {}
        )

    def getAllArrivalPredictions(self, modes: str, count: str):
        """
        Returns arrival predictions for all stops

        Args:
            modes: The modes for which to return predictions e.g. tube, dlr
            count: The number of predictions to return, -1 to return all available
        """

        return super(mode, self).sendRequestUnified(
            f"/Mode/{modes}/Arrivals", {'count': count}
        )
