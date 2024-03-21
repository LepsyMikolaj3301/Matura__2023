"""



"""
from math import sqrt


def liczba_prw(liczba):
    for j in range(2, int(liczba**1/2) + 1):
        if liczba % j == 0:
            return False
    return True


def zadanie1(tablica):
    odpowiedz = 0
    for liczby in tablica:
        if liczba_prw(liczby[0]) and liczba_prw(liczby[1]):
            odpowiedz += 1
    return odpowiedz


def zadanie2(tablica):
    odpowiedz = 0
    for liczby in tablica:
        if set(str(liczby[0])) == set(str(liczby[1])):
            odpowiedz += 1
    return odpowiedz


def odleglosc(zestaw1: list, zestaw2: list):
    odl_x = (zestaw2[0] - zestaw1[0])**2
    odl_y = (zestaw2[1] - zestaw1[1])**2
    odl = sqrt(odl_x + odl_y)
    return odl


def zadanie3(tablica):
    max_len = odleglosc(tablica[0], tablica[1])
    p1, p2 = tablica[0], tablica[1]
    for i in range(len(tablica)):
        for j in range(i + 1, len(tablica)):
            if odleglosc(tablica[i], tablica[j]) > max_len:
                max_len = odleglosc(tablica[i], tablica[j])
                p1 = tablica[i]
                p2 = tablica[j]
    return round(max_len), p1, p2


"""
punkty w danych 0 - 10 000


"""
def zadanie4(tablica):
    inside, on_line, outside = 0, 0, 0
    for punkt in tablica:
        # inside
        if punkt[0] < 5000 and punkt[1] < 5000:
            inside += 1
        if punkt[0] > 5000 or punkt[1] > 5000:
            outside += 1
        if punkt[0] == 5000 and punkt[1] < 5000:
            on_line += 1
        if punkt[1] == 5000 and punkt[0] < 5000:
            on_line += 1
    return inside, on_line, outside


def main():
    DANE = []
    with open("MIN-DANE-2017\\punkty.txt", 'r') as file:
        for line in file:
            DANE.append([int(i) for i in line.split()])
    print(f'Zadanie 1: {zadanie1(DANE)}')
    print(f'Zadanie 2: {zadanie2(DANE)}')
    odl, p1, p2 = zadanie3(DANE)
    print(f'Zadanie 3: \nodleglosc: {odl}\nPunkt A: {p1}\nPunkt B: {p2}')
    inside, on_line, outside = zadanie4(DANE)
    print(f'Zadanie4\nW srodku: {inside}\nna bokach: {on_line}\nna zewnatrz: {outside}')



main()
