from .tfl import tflAPI


class bikePoint(tflAPI):
    """Bike point from Unified API"""

    def getAll(self):
        """Gets all bike point locations"""
        return super(bikePoint, self).sendRequestUnified(
            "/BikePoint", {}
        )

    def getByID(self, ID):
        """
        Gets the bike point by the given id

        Args:
            ID: The ID of the bike point
        """
        return super(bikePoint, self).sendRequestUnified(
            f"/BikePoint/{ID}", {}
        )

    def getByName(self, name):
        """
        Search for bike points by their name

        Args:
            name: The name of the bike point
        """
        return super(bikePoint, self).sendRequestUnified(
            f"/BikePoint/Search", {'query': name}
        )
