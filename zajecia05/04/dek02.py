# porównaj z plikiem `dek01d.py`

import random
import time


# funkcja `frame` jest dekoratorem`
def frame(function):
    def wrapper():
        print('-----------------------------------')
        function()
        print('-----------------------------------\n')

    return wrapper


@frame  # w tym miejscu dekorujemy funkcję `calculations`, to jest dokładnie to samo co `calculations = frame(calculations)`
def calculations():
    # ta funkcja nie robi nic pożytecznego
    print('liczę', end='')
    for _ in range(5):
        print('.', end='', flush=True)
        time.sleep(0.5)
    print('obliczyłem! wynik to: ', random.randint(10, 100))


if __name__ == '__main__':
    calculations()
    calculations()
    calculations()
