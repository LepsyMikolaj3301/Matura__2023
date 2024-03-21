"""


"""

def zadanie2(tablica):
    haslo = ""
    j = 0
    for i in range(19, len(tablica), 20):
        haslo += tablica[i][j]
        j += 1
    return haslo

def palindrom(string):
    if string[::-1] == string:
        return True
    return False



def zadanie3(tablica):
    odp = ""
    for line in tablica:
        if palindrom(line[-1] + line):
            pal = line[-1] + line
            odp += pal[25]
        if palindrom(line + line[0]):
            pal = line + line[0]
            odp += pal[25]
    return odp

def cyfry_od_napis(napis):
    cyfry = ""
    for i in napis:
        if "0" <= i <= '9':
            cyfry += i
    return cyfry

def f_znaki(cyfry):
    litery = "" # 760945
    if len(cyfry) % 2 != 0:
        cyfry = cyfry[:-1]
    for i in range(0, len(cyfry), 2):
        dwoja = cyfry[i:i + 2]
        if 65 <= int(dwoja) <= 90:
            litery += chr(int(dwoja))
    return litery


def zadanie4(tablica):
    odp = ""
    for line in tablica:
        if odp[-3:] == "XXX":
            break
        else:
            odp += f_znaki(cyfry_od_napis(line))
    return odp

def main():
    DANE = []
    with open("DANE\\napisy.txt", 'r') as file:
        for line in file:
            DANE.append(line.rstrip())
    print(zadanie2(DANE))
    print(zadanie3(DANE))
    print(zadanie4(DANE))

main()