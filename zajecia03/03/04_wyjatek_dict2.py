# Uruchom skrypt raz z zakomentowaną linią 3, a raz z 4

samochod = {'nazwa': 'Fiat 126p', 'ilość_kół': 4}
# samochod = {'nazwa': 'Fiat 126p', 'ilość_kół': 4, 'rocznik': 1992}

rocznik = samochod.get('rocznik')  # zwraca None, jeśli słownik nie posiada danego klucza

print(f'rocznik samochodu {samochod["nazwa"]} to {rocznik}')
