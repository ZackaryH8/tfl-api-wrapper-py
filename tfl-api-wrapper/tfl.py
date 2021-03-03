import urllib.request
import urllib.parse
import json


unifiedAPI = "https://api.tfl.gov.uk"
trackerNetAPI = "http://cloud.tfl.gov.uk/TrackerNet"


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
        content = json.loads(
            resource.read().decode(resource.headers.get_content_charset())
        )
        return content

    @staticmethod
    def arrayToCSV(array):
        ",".join(array)
