import random
import time


def frame(function):
    def wrapper(*args, **kwargs):
        print('-----------------------------------')
        function(*args, **kwargs)
        print('-----------------------------------')

    return wrapper


@frame
def calculations(trudnosc=5):
    # ta funkcja nie robi nic pożytecznego
    print('liczę', end='')
    for _ in range(trudnosc):
        print('.', end='', flush=True)
        time.sleep(0.5)
    print('obliczyłem! wynik to: ', random.randint(10, 100))


@frame
def drukuj_argumenty(*args):
    for arg in args:
        print(arg)


if __name__ == '__main__':
    calculations(4)
    print()  # oddzielenie pustą linią

    drukuj_argumenty('dzień')
    drukuj_argumenty('dzień', 'dobry')
    drukuj_argumenty('dzień', 'dobry', 'Python!')
