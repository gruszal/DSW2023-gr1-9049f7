from pprint import pprint

from bs4 import BeautifulSoup

html_data = open('blogs.html', encoding='utf8').read()

soup = BeautifulSoup(html_data, "html.parser")

ul_tag_recent_posts = soup.find('ul', class_='list-recent-posts')

pprint(ul_tag_recent_posts)

all_li_tags = ul_tag_recent_posts.find_all('li')
print(all_li_tags)
