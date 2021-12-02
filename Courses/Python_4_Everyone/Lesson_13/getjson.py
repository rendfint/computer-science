import json
import urllib.request, urllib.parse, urllib.error

jsonurl = input("Enter JSON url: ")
if len(jsonurl) < 1 : jsonurl = "http://py4e-data.dr-chuck.net/comments_42.json"

connect = urllib.request.urlopen(jsonurl)
print("Retrieving", jsonurl)

data = connect.read().decode()
print("Retrieved", len(data), "characters")

getjson = json.loads(data)

counts = getjson["comments"]
print("Counts:", len(counts))

sum = sum( [int(num["count"]) for num in getjson["comments"]] )
print("Sum:", sum)