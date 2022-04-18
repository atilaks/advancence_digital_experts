import requests
import json
from code import ApiKeyException

"""API Geocode de Google: Aplicada a una clase con dos métodos para generar consultas.
        - Constructor: Recibe la llave de la API.
        - Métodos:
            + Get_request: Generando la url, devuelve el Json de respuesta de la API.
            + Get_coordinates: Extrae del archivo de respuesta las coordenadas de geolocalización."""

# TODO: REVISAR LINEAS DE LAS EXCEPCIONES


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
