from urllib import request
import requests
import urllib.request, urllib.error, urllib.parse
import xml.etree.ElementTree as ET
import ssl
import re
import requests

ctx = ssl.create_default_context()
ctx.check_hostname= False
ctx.verify_mode = ssl.CERT_NONE

sym = input('Enter Ticker: ')
url = f"https://www.nasdaq.com/feed/rssoutbound?symbol={sym}"

headers = {
  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}

response = requests.get(url, headers=headers)
data = response.text
tree = ET.fromstring(data)
# print ('Title', tree.find('channel')[0].text)
with open('api.csv', 'w') as op:
    op.write("Date | News\n")
for child in tree.findall('.//item'):
  Date = child.find('pubDate').text
  News = child.find('title').text
  with open('api.csv', 'a') as op:
    op.write(Date)
    op.write(' | ')
    op.write(News)
    op.write("\n")
a = open('api.csv').read()
b = re.sub('\+[0-9]+', '', a)
c = b.replace('  ', ' ')
with open('api.csv', 'w') as op:
    op.write(c)
  