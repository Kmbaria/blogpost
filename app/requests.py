import urllib.request, json
from .models import Quotes

base_url=None

def configure_request(app):
    global base_url
    base_url = app.config["API_BASE_URL"]
    print(base_url)

def get_quotes():

    with urllib.request.urlopen(base_url) as url:

        quotes_data = url.read()
        print(quotes_data)
        quotes_response = json.loads(quotes_data)
        return quotes_response