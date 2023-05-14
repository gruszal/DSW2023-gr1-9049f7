from pprint import pprint

from bs4 import BeautifulSoup

html_data = open('blogs.html', encoding='utf8').read()

soup = BeautifulSoup(html_data, "html.parser")

first_ul_tag = soup.ul
all_li_tags = first_ul_tag.find_all('li')

print(type(all_li_tags))
pprint(all_li_tags)

for li_tag in all_li_tags:
    print(li_tag.text)
    print(li_tag.attrs)  # klasy znacznika html
