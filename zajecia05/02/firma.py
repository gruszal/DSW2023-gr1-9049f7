from typing import List


class Pracownik:
    def __init__(self, imie: str, nazwisko: str, pensja: float):
        self.imie = imie
        self.nazwisko = nazwisko
        self.pensja = None

        self.ustaw_pensje(pensja)

    def __repr__(self):
        return f'Pracownik({self.imie}, {self.nazwisko})'

    def ustaw_pensje(self, pensja: float) -> None:
        if pensja < PLACA_MINIMALNA:
            raise ValueError(f'Proponowana pensja "{pensja}" jest niższa niż płaca minimalna.')
        self.pensja = pensja


class Menadzer(Pracownik):
    def __init__(self, imie: str, nazwisko: str, pensja: float):
        super().__init__(imie, nazwisko, pensja)
        self.podwladni: List[Pracownik] = []

    def dodaj_podwladnego(self, podwladny: Pracownik) -> None:
        self.podwladni.append(podwladny)


def wypisz_pensje(pracownicy: List[Pracownik]) -> None:
    for pracownik in pracownicy:
        print(f'{pracownik} : {pracownik.pensja} zł')


def przyznaj_podwyzke(pracownicy: List[Pracownik], procent: int) -> None:
    for pracownik in pracownicy:
        nowa_pensja = pracownik.pensja * (1 + (procent / 100))
        pracownik.ustaw_pensje(nowa_pensja)


if __name__ == '__main__':
    PLACA_MINIMALNA = 3490

    p1 = Pracownik('Eleonora', 'Marciniak', 5000)
    p2 = Pracownik('Henryk', 'Sikorski', 3490)
    m1 = Menadzer('Sylwia', 'Wiśniewska', 6000)

    pracownicy = [p1, p2, m1]

    m1.dodaj_podwladnego(p1)
    m1.dodaj_podwladnego(p2)

    print(m1.podwladni)
