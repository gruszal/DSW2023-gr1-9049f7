from bs4 import BeautifulSoup

html_data = open('blogs.html', encoding='utf8').read()

# https://beautiful-soup-4.readthedocs.io/en/latest/#quick-start
soup = BeautifulSoup(html_data, "html.parser")

first_ul_tag = soup.find('ul')

print(type(first_ul_tag))
print()
print(first_ul_tag.prettify())
