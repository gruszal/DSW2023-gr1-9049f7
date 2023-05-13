import random
import time


def frame_with_char(znak='-'):
    def frame(function):
        def wrapper():
            print(znak * 35)
            function()
            print(znak * 35)

        return wrapper

    return frame


@frame_with_char('#')  # w tym miejscu tworzony jest nowy dekorator `frame` z parametrem `#`
def calculations():
    # ta funkcja nie robi nic pożytecznego
    print('liczę', end='')
    for _ in range(5):
        print('.', end='', flush=True)
        time.sleep(0.5)
    print('obliczyłem! wynik to: ', random.randint(10, 100))


if __name__ == '__main__':
    calculations()
    print()  # oddzielenie pustą linią
    calculations()
    print()
    calculations()
