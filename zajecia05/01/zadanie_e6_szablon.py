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


# tutaj napisz klasę Menadzer

def wypisz_pensje(pracownicy):
    for pracownik in pracownicy:
        print(f'{pracownik} : {pracownik.pensja} zł')


def przyznaj_podwyzke(pracownicy, procent):
    for pracownik in pracownicy:
        nowa_pensja = pracownik.pensja * (1 + (procent / 100))
        pracownik.ustaw_pensje(nowa_pensja)


if __name__ == '__main__':
    PLACA_MINIMALNA = 3490

    p1 = Pracownik('Eleonora', 'Marciniak', 5000)
    p2 = Pracownik('Henryk', 'Sikorski', 3490)
    m1 = Menadzer('Sylwia', 'Wiśniewska', 6000)

    pracownicy = [p1, p2, m1]

    # tutaj dodaj obiektowi "m1" do listy "podwladni" obiekty "p1" oraz "p2"

    # tutaj wydrukuj podwładnych menadżerki "m1"
