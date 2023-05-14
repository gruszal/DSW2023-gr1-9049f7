import requests
from bs4 import BeautifulSoup

# możemy pobrać plik z sieci ...
html_data = requests.get('https://www.python.org/blogs/').text

# ... albo użyć lokalnie zapisanej kopii
html_data = open('blogs.html', encoding='utf8').read()

soup = BeautifulSoup(html_data, "html.parser")

print(soup.prettify())
