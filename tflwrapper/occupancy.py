from .tfl import tflAPI


class occupancy(tflAPI):
    """Occupancy from Unified API"""

    def getBikePointByIDs(self, ids):
        """
        Gets the occupancy data for bike points

        Args:
            ids: List of bike point IDs (Eg. ['BikePoints_208', 'BikePoints_209'])
        """
        return super(occupancy, self).sendRequestUnified(
            f"/Occupancy/BikePoints/{self.arrayToCSV(ids)}", {}
        )

    def getCarParkByID(self, id):
        """
        Gets the occupancy for a car park with a given id

        Args:
            id: Car park ID (Eg. 'CarParks_800468')
        """
        
        return super(occupancy, self).sendRequestUnified(
            f"/Occupancy/CarPark/{id}", {}
        )

    def getChargeConnectorByID(self, id):
        """
        Gets the occupancy for a charge connectors with a given id

        Args:
            id: Charge connector ID (Eg. 'ChargePointESB-UT06NW-1')
        """
        
        return super(occupancy, self).sendRequestUnified(
            f"/Occupancy/ChargeConnector/{id}", {}
        )

    def getAllCarParks(self):
        """Gets the occupancy for all car parks that have occupancy data"""
        
        return super(occupancy, self).sendRequestUnified(
            f"/Occupancy/CarPark", {}
        )

    def getAllChargeConnectors(self):
        """Gets the occupancy for all charge connectors"""
        
        return super(occupancy, self).sendRequestUnified(
            f"/Occupancy/ChargeConnector", {}
        )