imiona = ['Artur', 'Barbara', 'Czesław']

print(imiona)

nowe_imie = input('Proszę podać nowe imię: ')

if not nowe_imie:
    print('Pusty string to nie jest poprawne imię.')
elif nowe_imie not in imiona:
    imiona.append(nowe_imie)
else:
    print('Imię ', nowe_imie, 'jest już na liście, więc nie zostanie dodane')

print(sorted(imiona))
