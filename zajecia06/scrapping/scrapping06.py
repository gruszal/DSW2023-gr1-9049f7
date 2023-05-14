import requests
from bs4 import BeautifulSoup

html_data = open('blogs.html', encoding='utf8').read()

soup = BeautifulSoup(html_data, "html.parser")

python_logo = soup.select_one("img.python-logo")

image_path = python_logo['src']
filename = image_path.split('/')[-1]
print(image_path)

full_url = f'https://www.python.org/{image_path}'

response = requests.get(full_url, stream=True)

with open(filename, mode='wb') as f:
    f.write(response.content)
