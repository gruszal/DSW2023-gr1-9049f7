def verbose_addition(a, b):
    result = a + b
    print(f'{a} + {b} = {result}')
    return result


if __name__ == '__main__':
    func = verbose_addition  # uwaga, nie ma nawiasów!

    print(type(func))

    name = func.__name__  # w taki sposób pobieramy nazwę oryginalnego obiektu funkcji

    print(f'nazwa funkcji to: {name}')
