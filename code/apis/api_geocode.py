import os
import requests
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("key_google")


url = "https://maps.googleapis.com/maps/api/geocode/json?address=¨concepcion arenal, 12, valencia, 46470¨&key=" + token

response = requests.request("GET", url, headers={}, data={})

print(response.text)
