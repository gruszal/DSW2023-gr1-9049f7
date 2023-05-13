class Pracownik:
    def __init__(self, imie, nazwisko, pensja):
        self.imie = imie
        self.nazwisko = nazwisko
        self._pensja = self.sprawdz_pensje(pensja)  # uwaga! zmiana nazwy

    def __repr__(self):
        return f'Pracownik({self.imie}, {self.nazwisko})'

    def sprawdz_pensje(self, pensja):  # uwaga, ta funkcja nie używa "self"
        if pensja < PLACA_MINIMALNA:
            raise ValueError(f'Proponowana pensja "{pensja}" jest niższa niż płaca minimalna.')
        return pensja


if __name__ == '__main__':
    PLACA_MINIMALNA = 3490

    p1 = Pracownik('Eleonora', 'Marciniak', 5000)

    print(f'{p1}, pensja: {p1._pensja}')  # zauważ dostęp do atrybutu "protected"
