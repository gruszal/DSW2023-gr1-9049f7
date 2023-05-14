from bs4 import BeautifulSoup

html_data = open('blogs.html', encoding='utf8').read()

soup = BeautifulSoup(html_data, "html.parser")

first_ul_tag = soup.ul  # pierwszy napotkany tag 'ul'

print(type(first_ul_tag))
print()
print(first_ul_tag.prettify())

print(first_ul_tag.text)
print(first_ul_tag.name)
print(first_ul_tag.attrs)
print(first_ul_tag['class'])
