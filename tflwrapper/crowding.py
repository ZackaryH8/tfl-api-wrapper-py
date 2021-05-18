from .tfl import tflAPI


class crowding(tflAPI):
    """Crowding API"""

    def getByNaptan(self, naptanID: str):
        """Returns crowding information for Naptan"""

        return super(crowding, self).sendRequestUnified(
            f"/Crowding/{naptanID}", {}
        )

    def getByNaptanDay(self, naptanID: str, dayOfTheWeek: str):
        """
        Returns crowding information for Naptan for a specified day of week

        :param naptanID: ID of the stop (eg. 940GZZLUASL)
        :param dayOfTheWeek: The day of which you would like data to return (eg. MON, TUE, WED, THU, FRI, SAT, SUN)
        """

        return super(crowding, self).sendRequestUnified(
            f"/Crowding/{naptanID}/{dayOfTheWeek}", {}
        )
