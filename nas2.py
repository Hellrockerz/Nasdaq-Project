import requests
import xml.etree.ElementTree as ET
import ssl
import re
import csv

ctx = ssl.create_default_context()
ctx.check_hostname= False
ctx.verify_mode = ssl.CERT_NONE

sym = input('Enter Ticker: ').upper()
url = f"https://www.nasdaq.com/feed/rssoutbound?symbol={sym}"

headers = {
  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}

response = requests.get(url, headers=headers)
data = response.text
tree = ET.fromstring(data)

date = []
news = []

for child in tree.findall('.//item'):
  ate = child.find('pubDate').text

  Date = re.sub('\+[0-9]+', '', ate[5:])
  if Date not in date:
    date.append(Date)

  News = child.find('title').text
  if News not in news:
    news.append(News)

y = dict(zip(date, news))
print(y)

header = ['Date', 'News']