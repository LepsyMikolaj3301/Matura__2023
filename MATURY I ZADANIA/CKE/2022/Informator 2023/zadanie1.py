"""
Szachy



"""

def printing(tab):
    for i in tab:
        print(i)

def puste_kol(plansza):
    num_of_kolumny = 0
    for i in range(8):
        pust_kol = True
        for j in range(8):
            if plansza[j][i] != '.':
                pust_kol = False
        if pust_kol:
            num_of_kolumny += 1
    return num_of_kolumny

def zadanie1(tablica):
    m_puste_kolumny = 0
    m_naj_pus_kol = 0
    # serious >
    for i in range(9, len(tablica) + 2, 9):
        plansza = tablica[i-9:i-1]
        kolumny = puste_kol(plansza)
        if kolumny > 0:
            m_puste_kolumny += 1
            if kolumny > m_naj_pus_kol:
                m_naj_pus_kol = kolumny
    return m_puste_kolumny, m_naj_pus_kol



def rownowaga(plansza):
    black_pieces = []
    black_upper_p = []
    white_pieces = []
    on_l = ""
    for lines in plansza:
        on_l += lines
    s_plansza = []
    for l in on_l:
        if l != '.':
            s_plansza.append(l)
    for piece in s_plansza:
        if piece.isupper():
            white_pieces.append(piece)
        if piece.islower():
            black_pieces.append(piece)
    for b in black_pieces:
        black_upper_p.append(b.upper())
    # equal = True
    # if len(white_pieces) == len(white_pieces):
    #     for piec in black_upper_p:
    #         if piec not in white_pieces:
    #             equal = False
    if len(white_pieces) == len(black_upper_p):
        if white_pieces.sort() == black_upper_p.sort():
            return True, 2*len(white_pieces)
    return False, 0


def zadanie2(tablica):
    rownowagi = 0
    min_num_bierki = 20
    for i in range(9, len(tablica) + 2, 9):
        plansza = tablica[i-9:i-1]
        rowno, num_p = rownowaga(plansza)
        if rowno:
            rownowagi += 1
            if min_num_bierki > num_p:
                min_num_bierki = num_p
    return rownowagi, min_num_bierki



def szach_k_i_w(plansza):
    def szach_Kb(line, index_krola):
        for l in range(index_krola + 1, 8):
            if line[l] != '.' and line[l] != 'w' and line[l] != 'K':
                return False
            if line[l] == 'w':
                return True
        for l in range(index_krola, -1, -1):
            if line[l] != '.' and line[l] != 'w' and line[l] != 'K':
                return False
            if line[l] == 'w':
                return True
    def szach_k(line, index_krola):
        for l in range(index_krola, 8):
            if line[l] != '.' and line[l] != 'W' and line[l] != 'k':
                return False
            if line[l] == 'W':
                return True
        for l in range(index_krola, -1, -1):
            if line[l] != '.' and line[l] != 'W' and line[l] != 'k':
                return False
            if line[l] == 'W':
                return True

    k_y, k_x = 0, 0
    Kb_y, Kb_x = 0, 0
    Szach_Kb, Szach_k = False, False
    for index_y, line in enumerate(plansza):
        if "K" in line:
            Kb_y = index_y
            Kb_x = line.index("K")
        if "k" in line:
            k_y = index_y
            k_x = line.index('k')
    kol_k, wier_k = "", plansza[k_y]
    kol_Kb, wier_Kb = "", plansza[Kb_y]
    for i in range(8):
        kol_k += plansza[i][k_x]
    for j in range(8):
        kol_Kb += plansza[j][Kb_x]
    if szach_Kb(kol_Kb, Kb_y) or szach_Kb(wier_Kb, Kb_x):
        Szach_Kb = True
    if szach_k(kol_k, k_y) or szach_k(wier_k, k_x):
        Szach_k = True
    return Szach_Kb, Szach_k


def zadanie3(tablica):
    b_szach_k = 0
    cz_szach_K = 0
    for i in range(9, len(tablica) + 2, 9):
        plansza = tablica[i-9:i-1]
        sz_Kb, sz_k = szach_k_i_w(plansza)
        if sz_k:
            b_szach_k += 1
        if sz_Kb:
            cz_szach_K += 1
    return b_szach_k, cz_szach_K

def main():
    DANE_1 = []
    with open("Dane_2203\\szachy.txt", 'r') as file:
        for line in file:
            DANE_1.append(line.strip('\n'))
    print(zadanie1(DANE_1))
    print(zadanie2(DANE_1))
    print(zadanie3(DANE_1))

main()