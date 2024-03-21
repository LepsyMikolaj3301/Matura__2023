"""



"""


def horner(wsp: list, st: int, x: int):
    wynik = wspol[0]
    for i in range(1, st + 1):
        wynik = wynik * x + wsp[i]
    return wynik

wspol = [3, 4, 5, 7, 8]
stopien = len(wspol) - 1
argument = 1
print(horner(wspol, stopien, argument))
