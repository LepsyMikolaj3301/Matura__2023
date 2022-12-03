"""
    Napisz program, który wypełni macierz 5x5 liczbami parzystymi.
"""


def zadanie_5_1() -> list:
    table = [[] for _ in range(5)]
    iterajnik = 1
    for i in table:
        for j in range(5):
            i.append(iterajnik * 2)
            iterajnik += 1
    return table

print(zadanie_5_1())