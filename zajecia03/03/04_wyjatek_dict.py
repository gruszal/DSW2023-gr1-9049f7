# Uruchom skrypt raz z zakomentowaną linią 3, a raz z 4

samochod = {'nazwa': 'Fiat 126p', 'ilość_kół': 4}
# samochod = {'nazwa': 'Fiat 126p', 'ilość_kół': 4, 'rocznik': 1992}


try:
    rocznik = samochod['rocznik']
except KeyError:
    rocznik = None

print(f'rocznik samochodu {samochod["nazwa"]} to {rocznik}')
