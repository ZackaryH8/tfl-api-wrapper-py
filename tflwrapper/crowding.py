from .tfl import tflAPI


class crowding(tflAPI):
    """Crowding from Unified API"""

    def getallByNaptan(self, id):
        """
        Get crowding information for Naptan
        :param id: naptanID ID of the stop (eg. 940GZZLUASL)
        """
        return super(crowding, self).sendRequestUnified(
            f"/Crowding/{id}", {}
        )

    def getByNaptanDay(self, id, day):
        """
        Get crowding information for Naptan for a specified day of week
        :param day: The day of which you would like data to return (eg. MON, TUE)
        """
        return super(crowding, self).sendRequestUnified(
            f"/Crowding/{id}/{day}", {}
        )
