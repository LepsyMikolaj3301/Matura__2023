"""
https://arkusze.pl/matura-informatyka-2016-maj-poziom-rozszerzony/


1, 2, 3, {4, 5, 6 }, 7

"""


def cykl(liczba: int, od, do) -> int:
    len_oddo = do - od + 1
    while liczba > do:
        liczba -= len_oddo
    while liczba < od:
        liczba += len_oddo
    return liczba

def wylicz_klucz(alfa, beta) -> int:
    un_alfa, un_beta = ord(alfa), ord(beta)
    if un_beta > un_alfa:
        return un_beta - un_alfa
    else:
        return un_beta + 26 - un_alfa

def porownanie_szyfrogramow(slowo1: str, slowo2: str):
    klucz = wylicz_klucz(slowo1[0], slowo2[0])
    for i in range(len(slowo1)):
        if szyfr_cezara(slowo1[i], klucz) != slowo2[i]:
            return False
    else:
        return True


def szyfr_cezara(litera: str, klucz: int, deszyfr=False) -> str:
    litera_ascii = ord(litera)
    if deszyfr:
        klucz *= -1
    return chr(cykl(litera_ascii + klucz, 65, 90))


def zadanie6_1(tablica: list):
    klucz = 107
    with open("odpowiedzi\\wyniki_6_1.txt", 'w') as file:
        for slowo in tablica:
            for litera in slowo:
                file.write(szyfr_cezara(litera, klucz))
            file.write('\n')


def zadanie6_2(tablica: list):
    with open("odpowiedzi\\wyniki_6_2.txt", 'w') as file:
        for linia in tablica:
            lista = list(linia.split())
            if len(lista) > 1:
                szyfrogram, klucz = lista
                klucz = int(klucz)
                for i in szyfrogram:
                    file.write(szyfr_cezara(i, klucz, deszyfr=True))
                file.write('\n')
            else:
                file.write(szyfrogram + '\n')


def zadanie6_3(tablica: list):
    with open("odpowiedzi\\wyniki_6_3.txt", 'w') as file:
        for line in tablica:
            word1, word2 = line.split()
            if not porownanie_szyfrogramow(word1, word2):
                file.write(word1 + '\n')


def main():
    DANE = []
    with open("Dane_NOWA\\dane_6_3.txt", 'r') as f:
        for i in f:
            DANE.append(i.rstrip('\n'))
    # zadanie6_1(DANE)
    # zadanie6_2(DANE)
    zadanie6_3(DANE)


main()
