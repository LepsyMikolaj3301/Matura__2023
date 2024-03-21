"""
program na silnie

"""


def silnia_iteracyjnie(liczba:int):
    wynik = 1
    while liczba != 0:
        wynik *= liczba
        liczba -= 1
    return wynik

def silnia_rekurencyjnie(liczba:int):
    if liczba == 0:
        return 1
    return liczba * silnia_rekurencyjnie(liczba - 1)


print(silnia_iteracyjnie(0))
print(silnia_rekurencyjnie(0))