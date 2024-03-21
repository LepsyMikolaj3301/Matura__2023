"""
Pierwszą cyfrę mnożymy przez 1, 0%4 = 0
drugą cyfrę mnożymy przez 3, 1%4 = 1
trzecią cyfrę mnożymy przez 7, 2%4 = 2
czwarta cyfrę mnożymy przez 9,  3
piątą cyfrę mnożymy przez 1, 4%4 = 0
szóstą cyfrę mnożymy przez 3, 1
siódmą cyfrę mnożymy przez 7, 2
ósmą cyfrę mnożymy przez 9, 3
dziewiątą cyfrę mnożymy przez 1, 0
dziesiątą cyfrę mnożymy przez 3, 1
jedenastą cyfrę mnożymy przez 1.

"""


def pesel(nr_psl: str) -> bool:
    dzielniki = [1, 3, 7, 9]
    #            0, 1, 2, 3
    suma = 0
    for j in range(len(nr_psl) - 1):
        numer = int(nr_psl[j])
        iloczyn = numer * dzielniki[j % 4]
        suma += iloczyn
    suma += int(nr_psl[10])
    if suma % 10 == 0:
        return True
    else:
        return False

DANE = []
with open('PESEL.txt', 'r') as file:
    for line in file:
        DANE.append(line.rstrip('\n'))
proby = int(DANE[0])
for i in range(proby):
    pesel_ = DANE[i + 1]
    if pesel(pesel_):
        print('D')
    else:
        print('N')
