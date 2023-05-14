from pprint import pprint

import requests

# https://pokeapi.co/docs/v2
response = requests.get('https://pokeapi.co/api/v2/pokemon?offset=0&limit=5')

print(response.url)

odpowiedz = response.json()  # możemy od razu wczytać odpowiedź w formacie JSON jako obiekt pythonowy

print()

pprint(odpowiedz)

print(odpowiedz['next'])
