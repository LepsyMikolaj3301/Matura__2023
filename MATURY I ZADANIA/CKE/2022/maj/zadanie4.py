"""


"""

def zadanie1(tab):
    odp1 = 0
    for l in tab:
        if l[0] == l[-1]:
            odp1 += 1
            #print(l)
    return odp1

def rozklad(liczba):
    czyn = []
    j = 2
    while liczba > 1:
        if liczba % j == 0:
            czyn.append(j)
            liczba /= j
        else:
            j += 1
    return czyn

def zadanie2(tab):
    czyn_max = 0
    licz_czyn_max = 0
    czyn_roz = 0
    licz_czyn_roz = 0
    for i in tab:
        liczba = int(i)
        czynniki = rozklad(liczba)
        if licz_czyn_max < len(czynniki):
            licz_czyn_max = len(czynniki)
            czyn_max = liczba
        if licz_czyn_roz < len(set(czynniki)):
            licz_czyn_roz = len(set(czynniki))
            czyn_roz = liczba
    odp = [czyn_max, licz_czyn_max, czyn_roz, licz_czyn_roz]
    return odp

def trojka(x, y, z):
    if y % x == 0 and z % y == 0:
        return True
    return False

def any_ciag_dziel(tablica: list):
    for i in range(1, len(tablica)):
        if tablica[i] % tablica[i - 1] != 0:
            return False
    return True

def zadanie3(tab_n):
    tab = [int(j) for j in tab_n]
    odpowiedz1 = 0
    with open("odpowiedzi\\trojki.txt", 'w') as file:
        for i in range(2, len(tab)):
            if any_ciag_dziel(tab[i-2:i]):

                odpowiedz1 += 1
                file.write(f"{tab[i - 2]} {tab[i - 1]} {tab[i]}\n")
    odpowiedz2 = 0
    for i in range(4, len(tab)):
        new_tab = tab[i-5:i]
        if any_ciag_dziel(new_tab):
            odpowiedz2 += 1
    return odpowiedz1, odpowiedz2

def main():
    DANE = []
    with open("Dane_2205\\przyklad.txt", 'r') as file:
        for line in file:
            DANE.append(line.rstrip())


    z1 = zadanie1(DANE)
    z1a = 93639
    z2 = zadanie2(DANE)
    z3_1, z3_2 = zadanie3(DANE)

    with open("odpowiedzi\\wyniki4.txt", 'w') as f:
        f.write(f"4.1 {z1} {z1a} \n4.2 {z2} \n4.3 a) {z3_1}\nb) {z3_2}")


main()