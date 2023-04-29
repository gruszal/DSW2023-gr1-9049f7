lista_trzyelementowa = ['a', 'b', 'c']

try:
    trzynasty_element = lista_trzyelementowa[13]
except IndexError:
    print('Ktoś próbował sprawdzić wartość pod indeksem, którego nie ma!')

try:
    wynik_dzielenia_przez_zero = 13 / 0
except ZeroDivisionError:
    print('Ktoś próbował dzielić przez zero!')

print('Program działa dalej')
