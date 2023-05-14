from urllib.request import urlopen
import json

with urlopen('http://yesno.wtf/api') as response:
    odpowiedz_json = response.read()

odpowiedz = json.loads(odpowiedz_json)

print(odpowiedz)

url_zdjecia = odpowiedz['image']
print(url_zdjecia)

with urlopen(url_zdjecia) as response:
    odpowiedz = response.read()

nazwa = url_zdjecia.split('/')[-1]

with open(nazwa, mode='bw') as f:
    f.write(odpowiedz)
