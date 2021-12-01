import re
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input("Enter full url address: ")

if len(url) < 1 :
    url = "http://py4e-data.dr-chuck.net/comments_42.html"

html = urllib.request.urlopen(url).read()
bs_html = BeautifulSoup(html, "html.parser")
bs_span = bs_html("span")
lst_span = [str(n) for n in bs_span]
str_span = str(lst_span)

print( sum( [ int(x) for x in re.findall('[0-9]+', str_span) ] ) )
