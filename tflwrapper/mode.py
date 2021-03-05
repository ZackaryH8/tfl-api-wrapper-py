from .tfl import tflAPI


class mode(tflAPI):
    """Mode API"""

    def getActiveServiceTypes(self):
        """Returns the service type active for a mode, currently only supports tube"""

        return super(mode, self).sendRequestUnified(
            "/Mode/ActiveServiceTypes", {}
        )

    def getArrivalPredictionsAllStops(self, modes: str, count: str):
        """

        :param modes: A mode name e.g. tube, dlr
        :param count: A number of arrivals to return for each stop, -1 to return all available
        """

        return super(mode, self).sendRequestUnified(
            f"/Mode/{modes}/Arrivals", {'count': count}
        )
