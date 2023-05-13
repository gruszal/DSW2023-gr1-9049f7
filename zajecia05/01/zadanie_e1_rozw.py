class Pracownik:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

    def __repr__(self):
        return f'Pracownik({self.imie}, {self.nazwisko})'


if __name__ == '__main__':
    p1 = Pracownik('Eleonora', 'Marciniak')
    print(p1)

    p2 = Pracownik('Henryk', 'Sikorski')
    print(p2)
