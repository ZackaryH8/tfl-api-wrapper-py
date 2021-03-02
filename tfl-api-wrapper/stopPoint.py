import main
import urllib.request
import json


class stopPoint:

    def getcatergories(self):
        resource = urllib.request.urlopen(f"{main.unifiedAPI}/StopPoint/Meta/Categories")
        content = json.loads(resource.read().decode(resource.headers.get_content_charset()))
        return content
