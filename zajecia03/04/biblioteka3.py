def wypisz_ilosc_znakow_w_tekscie(tekst):
    ile_znakow = len(tekst)
    print(f'Tekst ma długość {ile_znakow} znaków')


przykladowy_tekst = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'

if __name__ == '__main__':  # "jeśli plik został uruchomiony bezpośrednio (niezaimportowany)"
    print(przykladowy_tekst)
    wypisz_ilosc_znakow_w_tekscie(przykladowy_tekst)
