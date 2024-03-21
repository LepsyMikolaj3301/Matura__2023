"""


"""
def zadanie4_1(tablica) -> int:
    ile_liczb = 0
    for liczba in tablica:
        ilosc_jeden, ilosc_zero = 0,0
        for i in liczba:
            if i == '1':
                ilosc_jeden += 1
            else:
                ilosc_zero += 1
        if ilosc_zero > ilosc_jeden:
            ile_liczb += 1
    return ile_liczb


def zadanie4_2(tablica: list):
    podz_2, podz_8 = 0, 0
    for liczba in tablica:
        liczba_tyl = liczba[::-1]
        if liczba_tyl[0] == '0':
            podz_2 += 1
        if liczba_tyl[:3] == '000':
            podz_8 += 1
    return podz_2, podz_8



def zamiana_bin_dzies(liczba_bin: str) -> int:
    liczba_od_tyl = liczba_bin[::-1]
    liczba_dz = 0
    for x, y in enumerate(liczba_od_tyl):
        liczba_dz += int(y) * (2 ** x)
    return liczba_dz


def zadanie4_3(tablica):
    tablica_dziesietne = []
    for liczba in tablica:
        tablica_dziesietne.append(zamiana_bin_dzies(liczba))
    index_min, index_max = 0,0
    for i in range(1, len(tablica_dziesietne)):
        if tablica_dziesietne[i] > tablica_dziesietne[index_max]:
            index_max = i
        if tablica_dziesietne[i] < tablica_dziesietne[index_min]:
            index_min = i
    return index_min + 1, index_max + 1


def main():
    DANE = []
    with open("Dane_PR\\liczby.txt", 'r') as file:
        for line in file:
            DANE.append(line.rstrip('\n'))
    zadanie1 = zadanie4_1(DANE)
    zadanie2 = list(zadanie4_2(DANE))
    zadanie3 = list(zadanie4_3(DANE))



    with open("wynik4.txt", 'w') as file_:
        file_.write("4.1 \nLiczba liczb zawierajacych wiecej 0 niz 1: " + str(zadanie1) + '\n' * 2)
        file_.write("4.2 \nLiczba liczb podzielnych przez 2: " + str(zadanie2[0]) + '\nLiczba liczb podzielnych przez 8: ' + str(zadanie2[1]) + '\n' * 2)
        file_.write("4.2 \nNumer wiersza z liczba najmniejsza: " + str(zadanie3[0]) + '\nNumer wiersza z liczba najwieksza: ' + str(zadanie3[1]))


main()
