imiona = ['Artur', 'Barbara', 'Waldemar']

for para in enumerate(imiona, start=1):
    print(para)
    dlugosc = len(para[1])
    print(para[0], ":", para[1] , ", liter:", dlugosc)
