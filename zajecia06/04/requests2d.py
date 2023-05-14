from pprint import pprint

import requests

# https://pokeapi.co/docs/v2
response = requests.get('https://pokeapi.co/api/v2/pokemon/pikachu')
response = requests.get('https://pokeapi.co/api/v2/pokemon/bulbasaur')

dane = response.json()  # możemy od razu wczytać odpowiedź w formacie JSON jako obiekt pythonowy

typy = [x['type']['name'] for x in dane['types']]

podsumowanie = f'{dane["name"]} ma id: {dane["id"]}, jest typu {typy}'
print(podsumowanie)
