class Pracownik:
    def __init__(self, imie, nazwisko, pensja):
        self.imie = imie
        self.nazwisko = nazwisko
        self._pensja = None  # "prawdziwy" atrybut przechowujący pensję

        self.pensja = pensja  # atrybut dostępny z zewnątrz

    def __repr__(self):
        return f'Pracownik({self.imie}, {self.nazwisko})'

    @property
    def pensja(self):
        return "xxx"  # dane poufne

    @pensja.setter
    def pensja(self, kwota):
        if kwota < PLACA_MINIMALNA:
            raise ValueError(f'Proponowana pensja "{kwota}" jest niższa niż płaca minimalna.')
        self._pensja = kwota


if __name__ == '__main__':
    PLACA_MINIMALNA = 3490

    p1 = Pracownik('Eleonora', 'Marciniak', 5000)

    print(f'{p1}, pensja: {p1.pensja}')
