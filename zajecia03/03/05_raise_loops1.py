for x in range(5):
    for y in range(5):
        for z in range(5):

            print(x, y, z)
            if x + y + z == 7:
                print('STOP!')
                break  # chcemy przerwać działanie wszyskich pętli, ale to nie zadziała...

print('koniec programu')