from statistics import mean

with open('dane.txt', mode='r', encoding='utf8') as plik:
    linie = plik.readlines()

wszystkie_punkty = []

for linia in linie:
    punkty = linia.split(',')

    suma = 0
    for punkt in punkty:
        punkt_int = int(punkt)
        suma += punkt_int

        wszystkie_punkty.append(punkt_int)

    print(f'W turnieju zdobyto: {suma} punktów')

print(f'Średnia punktów to: {sum(wszystkie_punkty) / len(wszystkie_punkty)}')
