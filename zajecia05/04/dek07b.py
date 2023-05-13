from functools import lru_cache
from time import sleep


@lru_cache
def dlugie_obliczenia(liczba):
    wynik = liczba
    print(liczba, end='', flush=True)
    for _ in range(4):
        wynik += liczba
        print(f' + {liczba}', end='', flush=True)
        sleep(0.5)

    print(f' = {wynik}', flush=True)
    return wynik


if __name__ == '__main__':
    print(dlugie_obliczenia(1))
    print(dlugie_obliczenia(2))
    print(dlugie_obliczenia(123))

    # jeszcze raz wołamy funkcję z tymi samymi parametrami
    print(dlugie_obliczenia(1))
    print(dlugie_obliczenia(2))
    print(dlugie_obliczenia(123))

    # a tu coś nowego
    print(dlugie_obliczenia(4))
