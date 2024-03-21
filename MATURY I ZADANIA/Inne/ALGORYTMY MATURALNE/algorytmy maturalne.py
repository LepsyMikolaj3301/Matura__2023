"""
ALGORYTMY MATURALNE


"""

#wyszukiwanie binarne

"""
dziel i zwyciężaj


"""

def wysz_bin_SETUP():
    tablica = [i + i for i in range(1000)]
    lewy = 0
    prawy = len(tablica) - 1

    szukana = int(input("Podaj wartosc"))

    def wysz_bin(szuk, l, p):
        if l < p:
            sr = (l + p) // 2
            if szuk <= tablica[sr]:
                return wysz_bin(szuk, l, sr)
            else:
                return wysz_bin(szuk, sr + 1, p)
        else:
            if tablica[p] == szuk:
                return p
            else:
                return -1

    return wysz_bin(szukana, lewy, prawy)

def alg_Euklidesa(num1, num2):
    r = num1 % num2
    if r == 0:
        return num2
    else:
        return alg_Euklidesa(num2, r)

def sito(n):
    tab = [True for _ in range(n)]
    tab[0], tab[1] = False, False
    for i in range(2, n):
        if tab[i]:
            for j in range(2*i, n, i):
                tab[j] = False
    num_pierwsze = []
    for index, l in enumerate(tab):
        if l:
            num_pierwsze.append(index)
    return num_pierwsze

def sort_bab(tab):
    """
    3, 2, 12, 4, 7, 8, 98

    """
    for j in range(len(tab)):
        for i in range(1, len(tab) - j):
            if tab[i - 1] < tab[i]:
                tab[i - 1], tab[i] = tab[i], tab[i - 1]
    return tab





"""
klucz = 3
arcw
A = 65
Z = 90
"""





def szyfr_cezara(slowo, klucz):
    def cycle(liczba):
        while 65 > liczba > 90:
            if liczba < 65:
                liczba += 90
    pass


def prz_kwd(liczba, dokladnosc):
    a = 1
    b = liczba
    for i in range(dokladnosc):
        a = (a + b) / 2
        b = liczba / a
    return a


if __name__ == "__main__":
    # print(sort_bab([3, 2, 12, 4, 7, 8, 98]))
    print(prz_kwd(3, 10))
