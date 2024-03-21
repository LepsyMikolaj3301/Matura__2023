"""
algorytm euklidesa:
a / b = c reszta R
-> b / R = d / R2


"""
import math


def potega_trzy(liczba):
    while liczba > 1:
        if liczba % 3 != 0:
            return False
        else:
            liczba /= 3
    return True


def zadanie1(table):
    odp = 0
    for num in table:
        if potega_trzy(num):
            odp += 1
    return odp


def suma_silni_check(num: int):
    def silnia(liczba):
        x = 1
        if liczba > 1:
            for i in range(2, liczba + 1):
                x *= i
        return x
    suma_silni = 0
    num_str = str(num)
    for j in num_str:
        suma_silni += silnia(int(j))
    if suma_silni == num:
        return True
    else:
        return False


def zadanie2(table):
    odp = []
    for number in table:
        if suma_silni_check(number):
            odp.append(number)
    return odp

"""
algorytm euklidesa:
a / b = c reszta R
-> b / R = d / R2
"""
def nwd(liczba1: int, liczba2: int) -> int:
    while liczba1 % liczba2 != 0:
        reszta = liczba1 % liczba2
        liczba1 = liczba2
        liczba2 = reszta
    return liczba1 % liczba2


"""
2 4 6 8 9
a_nwd = nwd(2,4)
if 

A = nwd(A, 6)


x1, x2, x3, x4, x5
3,   7,  4,  6, 10 , 2, 5
4,   6, 10,  2
A = nwd( x1, x2 )
nwd_a = nwd(A, x3)
if A > 1 and nwd > 1:
    
    A = nwd_a
else:
    
głupie
    
"""
def nwd_a(table):
#     zwroc: pierwsza liczba, dlg ciagu, NWD = A
    ciag_num, ciag_len, last_nwd = 0, 0, 0
    nwd_a = 0
    for index, i in enumerate(table[1:]):
        a = nwd(table[index - 1], i)
        if a > 1:
            if nwd(nwd_a, i) > 1:
                nwd_a = nwd(nwd_a, i)
            else:
                nwd_a = a
        #
        # else:



def na_int(table):
    n_table = []
    for i in table:
        n_table.append(int(i))
    return n_table

def main():
    DANE = []
    with open("Dane_PR\\przyklad.txt", 'r') as file:
        for line in file:
            DANE.append(int(line.rstrip()))
    DANE_int = na_int(DANE)



main()
