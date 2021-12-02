import xml.etree.ElementTree as ET
import urllib.request, urllib.parse, urllib.error
import re

xmlurl = input("Enter the XML url: ")
if len(xmlurl) < 1 : xmlurl = "http://py4e-data.dr-chuck.net/comments_42.xml"

connection = urllib.request.urlopen(xmlurl)
print("Retrieving", xmlurl)
data = connection.read().decode()
print("Data retrieved:", len(data), "characters")

tree = ET.fromstring(data)
numbers = tree.findall("comments/comment/count")
print("Count comments:", len(numbers))

sum = sum( [ int(number.text) for number in numbers ] )

print("Sum of counts:", sum)