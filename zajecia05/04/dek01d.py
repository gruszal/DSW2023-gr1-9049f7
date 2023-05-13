import random
import time


def frame(function):
    def wrapper():
        print('-----------------------------------')
        function()
        print('-----------------------------------\n')

    return wrapper


def calculations():
    # ta funkcja nie robi nic pożytecznego
    print('liczę', end='')
    for _ in range(5):
        print('.', end='', flush=True)
        time.sleep(0.5)
    print('obliczyłem! wynik to: ', random.randint(10, 100))


if __name__ == '__main__':
    calculations = frame(calculations)  # UWAGA! zapisujemy nową funkcję w miejsce poprzedniej!
    calculations()

    calculations()

    calculations()
