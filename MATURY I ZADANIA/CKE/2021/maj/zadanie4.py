"""



"""


def napis_kod(tablica_whole):
    napis = []

    def cycle(l):
        ord_l = ord(l)
        if ord_l == 90:
            return chr(65)
        return chr(ord_l + 1)

    for tablica in tablica_whole:
        komenda, litera = tablica[0], tablica[1]
        if komenda == 'DOPISZ':
            napis.append(litera)
        elif komenda == "ZMIEN":
            napis[-1] = litera
        elif komenda == "USUN":
            napis.pop()
        elif komenda == "PRZESUN":
            for i, j in enumerate(napis):
                if j == litera:
                    napis[i] = cycle(j)
                    break
    return napis

def ciag(tablica):
    komendy = []
    for i in tablica:
        komendy.append(i[0])
    najcz_kom, ile_r = komendy[0], 1
    ile = 1
    for j in range(1, len(komendy)):
        if komendy[j] == komendy[j - 1]:
            ile += 1
        else:
            if ile_r < ile:
                najcz_kom = komendy[j - 1]
                ile_r = ile
            ile = 1
    return najcz_kom, ile_r


def litera_ciag(tablica):
    def zlicz_z_tab(tablicza, znak):
        counter = 0
        for tab in tablicza:
            if tab[0] == "DOPISZ":
                if znak == tab[1]:
                    counter += 1
        return counter


    tab_l = []
    tab_lib = []
    for tab in tablica:
        if tab[0] == "DOPISZ":
            if tab[1] not in tab_l:
                tab_l.append(tab[1])
    for litera in tab_l:
        tab_lib.append(zlicz_z_tab(tablica, litera))
    maxin = tab_lib.index(max(tab_lib))
    return tab_l[maxin], max(tab_lib)





def main():
    DANE = []
    with open("DANE_2105\\instrukcje.txt", 'r') as file:
        for line in file:
            DANE.append(line.split())



    print(DANE[:20])
    print(ciag(DANE))
    print(litera_ciag(DANE))
    wynik_s = ''
    wynik = napis_kod(DANE)
    for i in wynik:
        wynik_s += i

    print(wynik_s)


main()
