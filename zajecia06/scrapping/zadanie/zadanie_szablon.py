from pprint import pprint

import requests
from bs4 import BeautifulSoup

html_data = requests.get('https://www.python.org/downloads/').text
# html_data = open('downloads.html', encoding='utf8').read()

soup = BeautifulSoup(html_data, "html.parser")

results = []

# tutaj napisz swój kod

pprint(results)
