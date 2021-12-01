import re
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input("Enter full url address: ")
if len(url) < 1 : url = "http://py4e-data.dr-chuck.net/known_by_Fikret.html"

url_position = input("Enter the position of the name you want to get: ")
if len(url_position) < 1 : url_position = "3"
url_position = int(url_position)

count = input("Amount of times to loop: ")
if len(count) < 1 : count = "4"
count = int(count)

names = re.findall('(?<=_by_).+(?=\.)', url)[0]

while count > 0:
    print("Retrieving: ", url)
    html = urllib.request.urlopen(url).read()
    bs_html = BeautifulSoup(html, "html.parser")
    bs_anchor = bs_html("a")
    find_url = bs_anchor[url_position - 1]
    find_url = str(find_url)
    new_url = re.findall('(?<=\").+(?=\")' , find_url)[0]
    find_name = str(bs_anchor[url_position - 1])
    name = re.findall('(?<=>).+(?=<)', find_name)[0]
    names = names + " - " + name
    count = count - 1
    url = new_url

print("\nAccessed the following names:", names, "\n")
