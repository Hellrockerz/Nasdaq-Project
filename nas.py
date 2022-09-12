from flask import Flask
from urllib import request
import requests
import urllib.request, urllib.error, urllib.parse
import xml.etree.ElementTree as ET
import ssl
headers = {
  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}
ctx = ssl.create_default_context()
ctx.check_hostname= False
ctx.verify_mode = ssl.CERT_NONE

import requests

sym = input('Enter Ticker: ')
url = f"https://www.nasdaq.com/feed/rssoutbound?symbol={sym}"

headers = {
  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}

response = requests.get(url, headers=headers)
data = response.text
tree = ET.fromstring(data)
print ('Title', tree.find('channel')[0].text)
for child in tree.findall('.//item'):
  print(child.find('title').text)
  print(child.find('pubDate').text, "\n")