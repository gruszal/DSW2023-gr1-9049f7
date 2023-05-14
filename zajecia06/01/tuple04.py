def podziel_stringa(tekst):
    lewa, separator, prawa = tekst.partition(',')

    return lewa, prawa


wynik = podziel_stringa('dzień dobry, dobry wieczór')

print(wynik)
print(type(wynik))

a, b = podziel_stringa('pierwszy,drugi')

print(a)
print(b)
