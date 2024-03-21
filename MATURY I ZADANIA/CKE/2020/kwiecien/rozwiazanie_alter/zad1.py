"""

4, 11, 4, 1, 4, 7, 11, 12, 13, 14, 7, 0, 3
4, 11, r = 7
11, 4, r
4, 1 ! r


"""


def luka(w1, w2) -> int:
    return abs(w1 - w2)


def zadanie_4_2(tablica):
    max_dl, dlugosc = 1, 2
    pierwszy = tablica[0]
    koncowy = tablica[0]
    r = luka(pierwszy, tablica[1])

    for index in range(1, len(tablica)):
        if luka(tablica[index], tablica[index - 1]) == r:
            dlugosc += 1
        else:
            dlugosc = 2
        if dlugosc >= max_dl:
            pierwszy = tablica[index - dlugosc + 1]
            koncowy = tablica[index]
            max_dl = dlugosc
        r = luka(tablica[index], tablica[index - 1])

    return max_dl, pierwszy, koncowy


def zadanie4_3()


def odczyt():
    with open("dane4.txt", 'r') as file:
        DANE = []
        for line in file:
            DANE.append(line.rstrip())
        for i in range(len(DANE)):
            DANE[i] = int(DANE[i])
    return DANE


def main():
    DANE = odczyt()
    tab = [4, 11, 4, 1, 4, 7, 11, 12, 13, 14, 7, 0, 3]
    print(zadanie_4_2(DANE))



main()