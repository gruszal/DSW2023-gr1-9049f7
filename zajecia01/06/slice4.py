lista = ['And', 'now', 'for', 'something', 'completely', 'different']

lista2 = lista[-2:]  # slice nie modyfikuje obiektu, ale tworzy NOWY na jego podstawie

print(lista)
print(lista2)

lista2[1] = 'New String'

print()

print(lista)
print(lista2)
