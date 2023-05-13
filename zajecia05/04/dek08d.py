class Pracownik:
    def __init__(self, imie, nazwisko, pensja):
        self.imie = imie
        self.nazwisko = nazwisko
        self.__pensja = None  # "prawdziwy" atrybut przechowujący pensję

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
        self.__pensja = kwota


if __name__ == '__main__':
    PLACA_MINIMALNA = 3490

    p1 = Pracownik('Eleonora', 'Marciniak', 5000)

    print(f'{p1}, pensja: {p1.pensja}')

    # print(f'{p1}, pensja: {p1.__pensja}')  # to nie zadziała
    # print(f'{p1}, pensja: {p1._Pracownik__pensja}')  # ale to już tak, nie da się zablokować dostępu do atrybutów
