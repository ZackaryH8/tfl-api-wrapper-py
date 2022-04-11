from .tfl import tflAPI


class crowding(tflAPI):
    """Crowding from Unified API"""

    def getAllByNaptan(self, id):
        """
        Get crowding information for Naptan

        Args:
            id: NaPTAN ID of the stop (eg. 940GZZLUASL)
        """
        return super(crowding, self).sendRequestUnified(
            f"/Crowding/{id}", {}
        )

    def getByNaptanDay(self, id, day):
        """
        Get crowding information for Naptan for a specified day of week

        Args:
            id: NaPTAN ID of the stop (eg. 940GZZLUASL)
            day: The day of which you would like data to return (eg. MON, TUE)
        """
        return super(crowding, self).sendRequestUnified(
            f"/Crowding/{id}/{day}", {}
        )

    def getLiveByNaptan(self, id):
        """
        Get crowding information for Naptan for a specified day of week

        Args:
            id: NaPTAN ID of the stop (eg. 940GZZLUASL)
        """
        return super(crowding, self).sendRequestUnified(
            f"/Crowding/{id}/Live", {}
        )
