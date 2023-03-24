import requests
import ssl
import re

ctx = ssl.create_default_context()
ctx.check_hostname= False
ctx.verify_mode = ssl.CERT_NONE

with open ('links.txt') as l:
    g = l.readlines()

for d in g:
    stripped = (d.rstrip())
    url = stripped+"/about"
    print("Retreiving" + url)
    response = requests.get(url)
    data = response.text
    link = re.findall('''(www.instagram.com.+?)\"''', data)
    ytName = re.findall(r"title\"\:\{\"simpleText\"\:\"(.+)\"avatar\"\:\{\"thumbnails\"\:", data)
    print(ytName)