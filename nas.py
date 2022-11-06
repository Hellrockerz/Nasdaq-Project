import requests
import xml.etree.ElementTree as ET
import ssl
import re
import csv
from flask import Flask
from flask_restful import Resource, Api
import pandas as pd

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

y = [list(x) for x in zip(date, news)]

header = ['Date', 'News']
content = y

with open('api.csv', 'w', encoding= 'UTF8', newline='') as file:
  writer= csv.writer(file)
  writer.writerow(header)
  writer.writerows(y)

app = Flask(__name__)
api= Api(app)
csv_path = './api.csv'
class api_data(Resource):
    def get(self):
        data = pd.read_csv(csv_path)
        data = data.to_dict()
        return {sym: data}, 200

api.add_resource(api_data, '/csv')

if __name__ == '__main__':
    app.run(debug=True)