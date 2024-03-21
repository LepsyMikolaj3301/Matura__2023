"""
MIN-R2A1P-153_dane

764321



"""
def zadanie6_1(tablica: list):
    odpowiedzi = []
    for kod in tablica:
        suma_p, suma_np = 0, 0
        for x, y in enumerate(kod):
            if x % 2 == 0:
                suma_p += int(y)
            else:
                suma_np += int(y)
        odpowiedzi.append(str(suma_p)+' '+str(suma_np))
    with open('odpowiedzi\\kody1.txt', 'w') as file:
        for line in odpowiedzi[:-1:]:
            file.write(line + '\n')
        file.write(odpowiedzi[-1])

def zsumowanie_cyfr(liczba: str) -> list:
    suma_p, suma_np = 0, 0
    for x, y in enumerate(liczba):
        if x % 2 == 0:
            suma_p += int(y)
        else:
            suma_np += int(y)
    return suma_p, suma_np


def kody_kreskowe() -> list:
    with open("MIN-R2A1P-153_dane\\cyfra_kodkreskowy.txt", 'r') as file:
        tablica = []
        for line in file:
            tablica.append(line)
    tablica = tablica[1:]
    tablica_kodow = []
    for i in tablica:
        kod = i.split()
        tablica_kodow.append(kod[1])
    return tablica_kodow

def cyfra_kontrolna(liczba: str) -> int:
    suma_p, suma_np = zsumowanie_cyfr(liczba)
    sum_sum = (3 * suma_p) + suma_np
    modulo_tej_liczby = sum_sum % 10
    wynik = (10 - modulo_tej_liczby) % 10
    return wynik

def liczba_na_kresk(cyfra: int) -> str:
    kody_krk = kody_kreskowe()
    return kody_krk[cyfra]


def Std_code_25(number: str) -> str:
    num_in_std_code_25 = ""
    start, stop = "11011010", "11010110"
    num_in_std_code_25 += start
    for i in number:
        num_in_std_code_25 += liczba_na_kresk(int(i))
    num_in_std_code_25 += liczba_na_kresk(cyfra_kontrolna(number))
    num_in_std_code_25 += stop
    return num_in_std_code_25


def zadanie6_2(tablica: list):
    with open('odpowiedzi\\kody2.txt', 'w') as file:
        for num in tablica[:-1:]:
            file.write(str(cyfra_kontrolna(num)) + ' ' + str(liczba_na_kresk(cyfra_kontrolna(num))) + '\n')
        file.write(str(cyfra_kontrolna(num[-1])) + ' ' + str(liczba_na_kresk(cyfra_kontrolna(num[-1]))))


def zadanie6_3(tablica: list):
    with open('odpowiedzi\\kody3.txt', 'a') as file:
        for num in tablica[:-1:]:
            file.write(Std_code_25(num) + '\n')
        file.write(Std_code_25(tablica[-1]))


def main():
    DANE = []
    with open("MIN-R2A1P-153_dane\\kody.txt", 'r') as file:
        for line in file:
            DANE.append(line.rstrip('\n'))
    zadanie6_1(DANE)
    zadanie6_2(DANE)
    zadanie6_3(DANE)
main()