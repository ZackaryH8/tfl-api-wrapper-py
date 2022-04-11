import json
import urllib.parse
import urllib.request
import urllib.error
import xmltodict
import datetime


class tflAPI(object):
    """TFL API"""

    def __init__(self, app_key):
        self.app_key = app_key

    def sendRequestUnified(self, uri: str, params = {}):
        """
        Send a HTTP GET request to the TFL Unified API using your API Key

        Args:
            uri: The URI to send the request to
            params: The parameters to send with the request
        
        Returns:
            The response from the TFL Unified API
        """
        fullURL = f"https://api.tfl.gov.uk:443{uri}?{urllib.parse.urlencode({'app_key': self.app_key})}"

        # If params is specified then convert it to a url encoded string
        if params:
            fullURL += f"&{urllib.parse.urlencode(params)}"

        # Send the request
        resource = urllib.request.urlopen(fullURL)
        
        return json.loads(
            resource.read().decode(resource.headers.get_content_charset())
        )

    @staticmethod
    def sendRequestTrackerNet(uri: str):
        """
        Send a HTTP GET request to the TrackerNet API

        Args:
            uri: The URI to send the request to
        
        Returns:
            The response from the TrackerNet API
        """

        data = urllib.request.urlopen(
            f"http://cloud.tfl.gov.uk/TrackerNet{uri}").read()

    @staticmethod
    def arrayToCSV(array):
        """
        Convert array to a comma-separated string
        
        Args:
            array: The array to convert to a comma-separated string
        
        returns:
            The comma-separated string
        """
        return ",".join(array)

    @staticmethod
    def getRFC3339(date_object):
        """
        Convert date object to RFC3339 standard
        
        Args:
            date_object: The date object to convert
        
        Returns:
            The RFC3339 formatted string
        """
        return date_object.isoformat("T") + "Z"
