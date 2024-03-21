""""
M, a, b

"""
def Mab(line):
    M, a, b = line.split()
    M, a, b = int(M), int(a), int(b)
    return M, a, b

def licz_pierwsza(liczba):
    for i in range(2, liczba):
        if liczba%i == 0:
            return False
    return True

def zadanie1(tab):
    odp = 0
    for line in tab:
        M, a, b = Mab(line)
        if licz_pierwsza(M):
            odp += 1
    return odp

def pasi(M, a, b):
    for x in range(0, M):
        if b == (a**x)%M:
            return True
    return False

def zadanie3(tab):
    odp = 0
    for line in tab:
        M, a, b = Mab(line)
        if pasi(M, a, b):
            odp += 1
    return odp



def main():
    DANE = []
    with open("Dane_2203\\liczby.txt", 'r') as file:
        for line in file:
            DANE.append(line.rstrip())
    with open("odpowiedzi\\wyniki3", 'w') as fum:
        fum.write(f'3.3 {zadanie1(DANE)}\n3.4\n3.5 ')



main()
