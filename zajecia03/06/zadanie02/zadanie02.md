# Zadanie 02 - zapis turnieju

W pliku `dane.txt` znajdziemy zapis punktów zdobytych przez gracza w turniejach. Każda linia to osobny turniej. 
W każdej linii wszystkie punkty oddzielone są przecinkiem.

Napisz program, który zsumuje ilość punktów zdobytych w każdym turnieju:

## Przykładowy wynik dla danych z `dane.txt`
```
W turnieju zdobyto: 10 punktów
W turnieju zdobyto: 6 punktów
W turnieju zdobyto: 13 punktów
```

## Podpowiedzi:
- możesz użyć metody `readlines()` pliku, aby wczytać na raz wszystkie linie z pliku do listy
- możesz użyć metody `split()` stringa, aby rozdzielić jeden string na listę stringów.
  - nalezy podać w parametrze, jaki znak ma być separatorem
- dane wczytane z pliku będą zawsze stringiem (lub bajtami, ale nie w tym przypadku). Pamiętaj, aby skonwertować string zawierający liczbę na typ `int`.

## Rozszerzenie
Policz średnią punktów zdobytych we wszystkich turniejach.
