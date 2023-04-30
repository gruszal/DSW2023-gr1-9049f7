with open('dane.txt', mode='r', encoding='utf8') as plik:
    linie = plik.readlines()

for linia in linie:
    punkty = linia.split(',')

    suma = 0
    for punkt in punkty:
        punkt_int = int(punkt)
        suma += punkt_int

    print(f'W turnieju zdobyto: {suma} punktów')
