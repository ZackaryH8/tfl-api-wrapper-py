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

        print(fullURL)

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
        print(json.dumps(xmltodict.parse(data)))

    @staticmethod
    def arrayToCSV(array):
        return ",".join(array)

    @staticmethod
    def getRFC3339(date_object):
        return date_object.isoformat("T") + "Z"
