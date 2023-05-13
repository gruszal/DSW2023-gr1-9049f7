class Pracownik:
    def __init__(self, imie, nazwisko, pensja):
        self.imie = imie
        self.nazwisko = nazwisko
        self.pensja = None

        self.ustaw_pensje(pensja)

    def __repr__(self):
        return f'Pracownik({self.imie}, {self.nazwisko})'

    def ustaw_pensje(self, pensja):
        if pensja < PLACA_MINIMALNA:
            raise ValueError(f'Proponowana pensja "{pensja}" jest niższa niż płaca minimalna.')
        self.pensja = pensja


if __name__ == '__main__':
    PLACA_MINIMALNA = 3490

    p1 = Pracownik('Eleonora', 'Marciniak', 5000)
    p2 = Pracownik('Henryk', 'Sikorski', 3490)
    p3 = Pracownik('Sylwia', 'Wiśniewska', 6000)

    # tutaj napisz pętlę wypisującą obecne pensje (etap 3)

    # tutaj napisz pętlę podnoszącą pensje (etap 4)

    print()  # pusta linia

    # tutaj napisz pętlę wypisującą obecne pensje (etap 4)
