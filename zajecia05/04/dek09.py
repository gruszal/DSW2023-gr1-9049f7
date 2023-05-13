class Punkt2d:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Punkt2d({self.x}, {self.y})"


if __name__ == '__main__':
    p = Punkt2d(5, 7)
    print(p)
