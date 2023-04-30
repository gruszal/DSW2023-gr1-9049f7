try:
    with open('plik_ktorego_nie_ma.txt', mode='r', encoding='utf8') as f:
        zawartosc = f.read()
    print(zawartosc)
except FileNotFoundError:
    print(f'Nie znaleziono pliku')
