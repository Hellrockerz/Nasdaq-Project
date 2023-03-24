# parse the html
import re
from bs4 import BeautifulSoup
import requests

url = "https://www.instagram.com/cinebapmrinmoy/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

print([e.get_text() for e in soup.select('._a3wf ._ac2a')])
