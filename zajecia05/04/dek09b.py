# https://docs.python.org/3/library/dataclasses.html
from dataclasses import dataclass


@dataclass
class Punkt2d:
    x: int
    y: int


if __name__ == '__main__':
    p = Punkt2d(5, 7)
    print(p)
