from math import pi

from geometria import pole_kola

wartosc = input('Podaj promień koła: ')
try:
    promien = float(wartosc)
    pole = pole_kola(promien, pi)
    print(f'Pole koła wynosi: {pole}')
except ValueError as ex:
    print(ex)
