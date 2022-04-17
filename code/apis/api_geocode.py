import requests
import json
from code import ApiKeyException


class ApiGeocode:
    def __init__(self, api_key):
        self._base_url = "https://maps.googleapis.com/maps/api/geocode/json?"
        if api_key is None:
            raise ApiKeyException()
        self._api_key = api_key

    def get_request(self, address):
        url = self._base_url + "address=" + address + "&key=" + self._api_key
        response = requests.request("GET", url, headers={}, data={})
        return json.loads(response.text)

    def get_coordinates(self, address):
        response = self.get_request(address)
        return response["results"][0]["geometry"]["location"]
