import random
import time


def calculations():
    # ta funkcja nie robi nic pożytecznego
    print('liczę', end='')
    for _ in range(5):
        print('.', end='', flush=True)
        time.sleep(0.5)
    print('obliczyłem! wynik to: ', random.randint(10, 100))


if __name__ == '__main__':
    print('-----------------------------------')
    calculations()
    print('-----------------------------------\n')

    print('-----------------------------------')
    calculations()
    print('-----------------------------------\n')

    print('-----------------------------------')
    calculations()
    print('-----------------------------------\n')
