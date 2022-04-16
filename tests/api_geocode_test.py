import os
import unittest
from code import ApiGeocode
from dotenv import load_dotenv
from code import ApiKeyException


class TestGeocode(unittest.TestCase):
    def test_rise_exception_for_none_api_key(self):
        self.assertRaises(ApiKeyException, lambda: ApiGeocode(None))

    def test_get_lat_and_lon(self):
        load_dotenv()
        self.token = os.getenv("key_google")
        self.geocode = ApiGeocode(self.token)
        expected = {"lat": 39.3977263, "lng": -0.3983829}

        address = "concepcion arenal, 12, valencia, 46470"
        request = self.geocode.get_coordinates(address)

        self.assertAlmostEqual(expected["lat"], request["lat"])
        self.assertAlmostEqual(expected["lng"], request["lng"])


if __name__ == '__main__':
    unittest.main()
