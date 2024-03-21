"""



"""

def liczba_pierwsza(num):
    for i in range(2, int(num**1/2 + 1)):
        if num % i == 0:
            return False
    return True


def zadanie1(tab):
    with open("odpowiedzi\\wyniki4_1.txt", 'w') as f:
        for num in tab:
            if liczba_pierwsza(num) and 100 <= num <= 5000:
                f.write(str(num) + "\n")
    return

def first_rev(num):
    if liczba_pierwsza(int(str(num)[::-1])):
        return True
    return False


def zadanie2(tab):
    with open("odpowiedzi\\wyniki4_2.txt", 'w') as file:
        for num in tab:
            if first_rev(num):
                file.write(str(num) + '\n')
    return


def waga(n):
    while len(str(n)) > 1:
        suma = 0
        for i in str(n):
            suma += int(i)
        n = suma
    return n

def zadanie3(tab):
    odpowiedz = 0
    for num in tab:
        if waga(num) == 1:
            odpowiedz += 1
    return odpowiedz

def main():
    DANE_liczby = []
    DANE_pierwsze = []
    with open("MIN-R2A1P-193_dane\\liczby_przyklad.txt", 'r') as file:
        for line in file:
            DANE_liczby.append(int(line.strip()))
    with open("MIN-R2A1P-193_dane\\pierwsze_przyklad.txt", 'r') as file:
        for line in file:
            DANE_pierwsze.append(int(line.strip()))
    # print(DANE_liczby)
    # zadanie1(DANE_liczby)
    zadanie2(DANE_pierwsze)
    print(zadanie3(DANE_pierwsze))

main()