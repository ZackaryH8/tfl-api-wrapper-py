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

    def sendRequestUnified(self, uri: str, params):
        """
        Send a HTTP GET request to the TFL Unified API using your API Key

        :param uri: The url which will be prepended to unifiedAPI
        :param params: An object containg any extra parameters
        :returns: API Data from TfL Unified API
        """
        fullURL = f"https://api.tfl.gov.uk:443{uri}?{urllib.parse.urlencode({'app_key': self.app_key})}"

        if params:
            fullURL += f"&{urllib.parse.urlencode(params)}"

        resource = urllib.request.urlopen(fullURL)
        return json.loads(
            resource.read().decode(resource.headers.get_content_charset())
        )

    @staticmethod
    def sendRequestTrackerNet(uri: str):
        """
        Send a HTTP GET request to the TrackerNet API

        :param uri: The url which will be prepended to trackerNetAPI
        :returns: API Data from TfL Unified API
        """

        data = urllib.request.urlopen(
            f"http://cloud.tfl.gov.uk/TrackerNet{uri}").read()

    @staticmethod
    def arrayToCSV(array):
        """
        Convert array to a comma-separated string

        :param array: Array to convert to a comma-separated string
        :returns: A comma-separated string
        """
        return ",".join(array)

    @staticmethod
    def getRFC3339(date_object):
        """
        Convert date object to RFC3339 standard

        :param date_object: A date object to convert to RFC3339 standard
        :returns: A RFC3339 formatted string
        """
        return date_object.isoformat("T") + "Z"
