from .tfl import tflAPI


class accidentStats(tflAPI):
    """Accident from Unified API"""

    def getAllByYear(self, year: int):
        """
        Gets all accident details for accidents occuring in the specified year

        Args:
            year: The year for which to filter the accidents on.
        """
        return super(accidentStats, self).sendRequestUnified(
            f"/AccidentStats/{year}"
        )
