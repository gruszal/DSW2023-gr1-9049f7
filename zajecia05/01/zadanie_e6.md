# Zadanie - Pracownik

## Etap 6

Stwórz klasę `Menadzer` dziedziczącą po klasie `Pracownik`. 
Nowa klasa ma mieć zaimplementowaną jedynie metodę `__init__`, która ma zawołać metodę `__init__` klasy nadrzędnej.
Nowa klasa ma mieć również dodany atrybut `podwladni`, który przy tworzeniu obiektu ma być ustawiony na pustą listę.

Następnie w bloku "main" należy dodać menadżerce `m1` podwładnych `p1` oraz `p2` a następnie wydrukować zawartość atrybutu `podwladni` obiektu `m1` na ekran.

## Rozszerzenie

Napisz metodę `dodaj_podwladnego` w klasie `Menadzer`, która będzie przyjmować jako parametr obiekt klasy `Pracownik` a następnie doda ten obiekt do listy `podwladni` klasy `Menadzer`. 

Zmień linijki dodające podwładnego, aby uzywały metody `dodaj_podwladnego`.
