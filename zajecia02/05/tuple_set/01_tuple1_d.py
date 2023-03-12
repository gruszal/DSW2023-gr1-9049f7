adres = ('Fundacja Python',
         'ul. Programistyczna 12',
         '00-001 Warszawa')

# Jeśli nie planujemy użyć którejś z wartości z tupli, możemy użyć w jej miejscu znaku "_"
nazwa, ulica, _ = adres

print(nazwa)
print(ulica)
