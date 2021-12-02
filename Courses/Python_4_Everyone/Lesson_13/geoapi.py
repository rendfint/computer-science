import json
import urllib.request, urllib.parse, urllib.error

key = False

location = input("Enter the location: ")
if len(location) < 1 : location = "South Federal University"

if key is False :
    key = "42"
else :
    key = input("Enter API key: ")

service_url = "https://py4e-data.dr-chuck.net/json?"

params = dict()
params["key"] = key
params["address"] = location

query_url = service_url + urllib.parse.urlencode(params)

connect = urllib.request.urlopen(query_url)
print("Retrieving", query_url)
data = connect.read()
print("Retrieved", len(data))
json_data = json.loads(data)

results = json_data["results"]
place_id = [place["place_id"] for place in results]

print("Place id:" ,place_id[0])