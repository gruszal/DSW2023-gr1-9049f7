class Pracownik:
    def __init__(self, imie, nazwisko, pensja):
        self.imie = imie
        self.nazwisko = nazwisko
        self.pensja = self.sprawdz_pensje(pensja)

    def __repr__(self):
        return f'Pracownik({self.imie}, {self.nazwisko})'

    @staticmethod
    def sprawdz_pensje(pensja):
        if pensja < PLACA_MINIMALNA:
            raise ValueError(f'Proponowana pensja "{pensja}" jest niższa niż płaca minimalna.')
        return pensja


if __name__ == '__main__':
    PLACA_MINIMALNA = 3490

    p1 = Pracownik('Eleonora', 'Marciniak', 5000)
    print(p1)
