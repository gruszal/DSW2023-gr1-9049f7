def verbose_addition(a, b):
    result = a + b
    print(f'{a} + {b} = {result}')
    return result


if __name__ == '__main__':
    func = verbose_addition  # uwaga, nie ma nawiasów!

    print(type(func))

    result = func(13, 17)

    print(result)

    print("Czy to jest ten sam obiekt?", func is verbose_addition)
