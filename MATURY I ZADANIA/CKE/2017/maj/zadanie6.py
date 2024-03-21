"""
       k
wiersz[0] 0 1 0 2
wiersz 0 0 1 0
wiersz 0 2 3 0

1. porównanie wiersz == wiersz + 1 ( ogranicz z dołu )
2. porównanie wiersz == wiersz - 1  ogranicz z góry
3. porównanie kolumna == kolumna + 1
4. porównanie kolumna == kolumna - 1

#
# def wiersz(tab: list)-> list:
#     tablica_koordy_w = []
#     for index, wiersz in enumerate(tab[:-1]):
#         for i, value in enumerate(wiersz): #
#             if sasiad_is_kontrast(int(value), int(tab[index + 1][i])):
#                 koordy = tuple([index, i])
#                 if koordy not in tablica_koordy_w:
#                     tablica_koordy_w.append(koordy)
#     for index, wiersz in enumerate(tab[1:]):
#         for i, value in enumerate(wiersz): #
#             if sasiad_is_kontrast(int(value), int(tab[index - 1][i])):
#                 koordy = tuple([index, i])
#                 if koordy not in tablica_koordy_w:
#                     tablica_koordy_w.append(koordy)
#     return tablica_koordy_w
#
# def kolumny(tab: list)-> list:
#     tablica_koordy_k = []
#     # tab[ i ] [ j ]
#     # od lewej do prawej
#
#     for j in range(319):
#         for i in range(200):
#             if sasiad_is_kontrast(int(tab[i][j]), int(tab[i][j + 1])):
#                 koordy = tuple([i, j])
#                 if koordy not in tablica_koordy_k:
#                     tablica_koordy_k.append(koordy)
#     # od prawej do lewej
#     for j in range(1, 320):
#         for i in range(200):
#             if sasiad_is_kontrast(int(tab[i][j]), int(tab[i][j - 1])):
#                 koordy = tuple([i, j])
#                 if koordy not in tablica_koordy_k:
#                     tablica_koordy_k.append(koordy)
#     return tablica_koordy_k
#


"""
def zadanie1(tablica):
    jasnosc_max = int(tablica[0][0])
    jasnosc_min = int(tablica[0][0])
    for i in tablica:
        for y in i:
            if int(y) > jasnosc_max:
                jasnosc_max = int(y)
            elif int(y) < jasnosc_min:
                jasnosc_min = int(y)
    return jasnosc_min, jasnosc_max


def wiersz_is_symetryczny(wiersz: list) -> bool:
    start, koniec = 0, 319
    while start < koniec:
        if wiersz[start] != wiersz[koniec]:
            return False
        start += 1
        koniec -= 1
    return True


def zadanie2(tablica):
    odpowiedz = 0
    for line in tablica:
        if not wiersz_is_symetryczny(line):
            odpowiedz += 1
    return odpowiedz


def sasiad_is_kontrast(piksel1, piksel2) -> bool:
    piksel1, piksel2 = int(piksel1), int(piksel2)
    if piksel1 < piksel2:
        piksel1, piksel2 = piksel2, piksel1
    if piksel1 - piksel2 > 128:
        return True
    return False

def rogi(tab: list):
    ilosc_kontrast = 0
    # lewy górny róg
    if sasiad_is_kontrast(tab[0][0], tab[0][1]) or sasiad_is_kontrast(tab[0][0], tab[1][0]):
        ilosc_kontrast += 1
    # lewy dolny róg
    if sasiad_is_kontrast(tab[199][0], tab[198][0]) or sasiad_is_kontrast(tab[199][0], tab[199][1]):
        ilosc_kontrast += 1
    # prawy górny róg
    if sasiad_is_kontrast(tab[0][319], tab[0][318]) or sasiad_is_kontrast(tab[0][319], tab[1][319]):
        ilosc_kontrast += 1
    # prawy dolnmy róg
    if sasiad_is_kontrast(tab[199][319], tab[198][319]) or sasiad_is_kontrast(tab[199][319], tab[199][318]):
        ilosc_kontrast += 1
    return ilosc_kontrast

def sciany(tab: list):
    """
    index - 1 | 0, index | index + 1
                1
    """
    # gora dol
    ilosc_kontrastow = 0
    for i in range(1, 319):
        poprzedni_g = sasiad_is_kontrast(tab[0][i], tab[0][i - 1])
        nastepny_g = sasiad_is_kontrast(tab[0][i], tab[0][i + 1])
        dolny_g = sasiad_is_kontrast(tab[0][i], tab[1][i])
        if poprzedni_g or nastepny_g or dolny_g:
            ilosc_kontrastow += 1
        poprzedni_d = sasiad_is_kontrast(tab[199][i], tab[199][i - 1])
        nastepny_d = sasiad_is_kontrast(tab[199][i], tab[199][i + 1])
        gorny_d = sasiad_is_kontrast(tab[199][i], tab[198][i])
        if poprzedni_d or nastepny_d or gorny_d:
            ilosc_kontrastow += 1
    # lewo prawo
    for i in range(1, 199):
        poprzedni_l = sasiad_is_kontrast(tab[i][0], tab[i - 1][0])
        nastepny_l = sasiad_is_kontrast(tab[i][0], tab[i + 1][0])
        prawy_l = sasiad_is_kontrast(tab[i][0], tab[i][1])
        if poprzedni_l or nastepny_l or prawy_l:
            ilosc_kontrastow += 1
        poprzedni_p = sasiad_is_kontrast(tab[i][319], tab[i - 1][319])
        nastepny_p = sasiad_is_kontrast(tab[i][319], tab[i + 1][319])
        lewy_p = sasiad_is_kontrast(tab[i][319], tab[i][318])
        if poprzedni_p or nastepny_p or lewy_p:
            ilosc_kontrastow += 1
    return ilosc_kontrastow

def siatka(tab: list):
    ilosc_kontrastow = 0
    for i in range(1, 199):
        for j in range(1, 319):
            # gora dol prawa lewa dla kazdego punktu
            gora = sasiad_is_kontrast(tab[i][j], tab[i - 1][j])
            dol = sasiad_is_kontrast(tab[i][j], tab[i + 1][j])
            prawo = sasiad_is_kontrast(tab[i][j], tab[i][j + 1])
            lewo = sasiad_is_kontrast(tab[i][j], tab[i][j - 1])
            if gora or dol or prawo or lewo:
                ilosc_kontrastow += 1
    return ilosc_kontrastow

def zadanie3(tablica):
    ilosc_kontrastow_all = 0
    ilosc_kontrastow_all += rogi(tablica)
    ilosc_kontrastow_all += sciany(tablica)
    ilosc_kontrastow_all += siatka(tablica)
    return ilosc_kontrastow_all

def longest_in_column(lista: list) -> int:
    length = 1
    current_number = lista[0]
    longest = length
    for i in range(1, 200):
        if current_number == lista[i]:
            length += 1
        else:
            if length > longest:
                longest = length
            length = 1
            current_number = lista[i]
    return longest
# dla danych działa, dla przyklad już nie


def zadanie4(tablica):
    dlg_najd_linii = 0
    for j in range(320):
        table = []
        for i in range(200):
            table.append(tablica[i][j])
        longest_line = longest_in_column(table)
        if longest_line > dlg_najd_linii:
            dlg_najd_linii = longest_line
    return dlg_najd_linii


def info1(tablica):
    wiersze, kolumny = 0, 0
    wiersze = len(tablica)
    kolumny = len(tablica[0])
    print(wiersze, ' ', kolumny)
    # 200 wierszy
    # 320 kolumn
    print(tablica[199][319])


def main():
    DANE = []
    with open("Dane_PR\\dane.txt", 'r') as f:
        for line in f:
            DANE.append(line.split())
    print(zadanie4(DANE))


main()