from pprint import pprint

import requests

# https://pokeapi.co/docs/v2

parametry = {
    'offset': 0,
    'limit': 5
}

response = requests.get('https://pokeapi.co/api/v2/pokemon', params=parametry)

print(response.url)

odpowiedz = response.json()  # możemy od razu wczytać odpowiedź w formacie JSON jako obiekt pythonowy

print()

pprint(odpowiedz)

print(odpowiedz['next'])
