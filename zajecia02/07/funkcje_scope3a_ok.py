lista = ['a', 'b']

print(lista)


def funkcja(lista):
    lista.append('c')
    print('wewnątrz funkcji:', lista)


funkcja(lista)
print(lista)
