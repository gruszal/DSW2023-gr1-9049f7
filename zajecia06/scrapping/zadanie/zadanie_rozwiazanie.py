from pprint import pprint

import requests
from bs4 import BeautifulSoup

# html_data = requests.get('https://www.python.org/downloads/').text
html_data = open('downloads.html', encoding='utf8').read()

soup = BeautifulSoup(html_data, "html.parser")

results = []

for li in soup.ol.find_all('li'):
    result = {
        'version': li.select_one('span.release-version').text,
        'release_end': li.select_one('span.release-end').text,
        'pep': li.select_one('span a')['href']
    }
    results.append(result)

pprint(results)
