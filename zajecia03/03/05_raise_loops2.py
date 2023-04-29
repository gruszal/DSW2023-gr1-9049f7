try:

    for x in range(5):
        for y in range(5):
            for z in range(5):

                print(x, y, z)
                if x + y + z == 7:
                    raise ValueError
except ValueError:
    print('STOP!')

print('koniec programu')