"""




"""


def babelkowe(tablica: list):
    for dlugosc in range(len(tablica), 0, -1):
        for i in range(dlugosc - 1):
            if tablica[i] > tablica[i + 1]:
                tablica[i], tablica[i + 1] = tablica[i + 1], tablica[i]
    return tablica


lista = [int(i) for i in "2,3,4,63,434,2,43,1,9".split(',')]
print(babelkowe(lista))
