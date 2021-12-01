import socket
import re

url_name = input("Enter url: ")

if len(url_name) < 1 :
    url_name = "http://data.pr4e.org/intro-short.txt"

host = re.findall('(?<=://)[\w-]+(?:\.[\w-]+)+', url_name)

opensock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
opensock.connect((host[0], 80))
cmd = ("GET " + url_name + " HTTP/1.0\r\n\r\n").encode()
opensock.send(cmd)

while True :
    data = opensock.recv(256)
    if len(data) < 1 :
        break
    print(data.decode())

opensock.close()

