import json

with open("api_geocode_response.json") as file:
    prueba = json.loads(file.read())


print(prueba["results"][0]["geometry"]["location"]["lat"])
print(prueba["results"][0]["geometry"]["location"]["lng"])

print(prueba["results"][0]["geometry"]["location"])
