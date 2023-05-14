import requests

html_data = requests.get('https://www.python.org/blogs/').text

print(html_data)

# możemy zapisać ten plik, by przy następnych testach pracować na lokalnych danych
with open('blogs.html', mode='w', encoding='utf8') as file:
    file.write(html_data)
