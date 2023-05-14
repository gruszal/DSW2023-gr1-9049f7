from pprint import pprint

from bs4 import BeautifulSoup

html_data = open('blogs.html', encoding='utf8').read()

soup = BeautifulSoup(html_data, "html.parser")

# uzycie selektora CSS: https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Selectors
all_li_tags = soup.select("ul.list-recent-posts li")

print(all_li_tags)
