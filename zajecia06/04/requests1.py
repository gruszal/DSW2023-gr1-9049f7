# https://requests.readthedocs.io/en/latest/
import requests

response = requests.get('http://yesno.wtf/api')

odpowiedz = response.json()  # możemy od razu wczytać odpowiedź w formacie JSON jako obiekt pythonowy

print(odpowiedz)
print(type(odpowiedz))

print(odpowiedz['answer'])
