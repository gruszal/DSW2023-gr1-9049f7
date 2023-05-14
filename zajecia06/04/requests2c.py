from pprint import pprint

import requests

# https://pokeapi.co/docs/v2
response = requests.get('https://pokeapi.co/api/v2/pokemon/pikachu')

dane = response.json()  # możemy od razu wczytać odpowiedź w formacie JSON jako obiekt pythonowy

podsumowanie = f'{dane["name"]} ma id: {dane["id"]}, jest typu {dane["types"]}'
print(podsumowanie)
