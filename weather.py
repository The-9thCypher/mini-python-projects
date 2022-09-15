import http.client
from pprint import pprint

conn = http.client.HTTPSConnection("weatherbit-v1-mashape.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': "f575e13156mshe3186d95355ce2cp1eb69djsn7038ecc9d0f8",
    'X-RapidAPI-Host': "weatherbit-v1-mashape.p.rapidapi.com"
    }

conn.request("GET", "/current?lon=38.5&lat=-78.5", headers=headers)

res = conn.getresponse()
data = res.read()

pprint(data)