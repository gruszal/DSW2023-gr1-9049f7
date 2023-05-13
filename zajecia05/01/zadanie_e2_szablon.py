class Pracownik:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

    def __repr__(self):
        return f'Pracownik({self.imie}, {self.nazwisko})'

    # tutaj dodaj metodę `ustaw_pensje`

if __name__ == '__main__':
    p1 = Pracownik('Eleonora', 'Marciniak', 5000)
    print(p1)

    p2 = Pracownik('Henryk', 'Sikorski', 3000)
    print(p2)
