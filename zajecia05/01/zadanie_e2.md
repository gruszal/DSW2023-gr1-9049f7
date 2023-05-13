# Zadanie - Pracownik

## Etap 2
Od początku 2023 roku płaca minimalna wynosi 3490 zł. Zmodyfikuj klasę z poprzedniego etapu dodając do metody `__init__` parametr `pensja` oraz dodając do klasy metodę `ustaw_pensje`.
Metoda `ustaw_pensje` ma przymować jeden parametr `pensja` i zwracać przekazaną pensję, jeśli jest poprawna (wyższa lub równa płacy minimalnej), lub rzucać wyjątek `ValueError` jeśli przekazana pensja nie spełnia wymogów prawnych.
Powyższa metoda powinna być użyta w metodzie `__init__` podczas tworzenia nowego obiektu.

**UWAGA** W tym przypadku skrypt ma zakończyć działanie rzuceniem wyjątku.

## Spodziewany wynik (uproszczony)
```
Pracownik(Eleonora, Marciniak)
Traceback (most recent call last):
  File "zadanie_e2_rozw.py", line 21, in <module>
    p2 = Pracownik('Henryk', 'Sikorski', 3000)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "zadanie_e2_rozw.py", line 5, in __init__
    self.pensja = self.ustaw_pensje(pensja)
                  ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "zadanie_e2_rozw.py", line 13, in ustaw_pensje
    raise ValueError(f'Proponowana pensja "{pensja}" jest niższa niż płaca minimalna.')
ValueError: Proponowana pensja "3000" jest niższa niż płaca minimalna.
```
