# funkcja, która przyjmuje jeden parametr i nie zwraca (wprost) żadnej wartości


def wydrukuj_dodanie_sto(liczba):
    wynik = liczba + 100
    print(f'{liczba} + 100 = {wynik}')


wartosc = 23

# funkcja, która nie ma wewnątrz swojego bloku wyrażenia `return` zwraca `None`
# prawdopodobnie, tak należy użyć tej funkcji
wydrukuj_dodanie_sto(wartosc)
