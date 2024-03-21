"""



"""


def odczyt1(string):
    dane = []
    with open(f"NM_DANE_PR\\{string}", 'r') as file:
        for line in file:
            dane.append([int(i) for i in line.split()])
    return dane


def zadanie1(tab1, tab2):
    odp = 0
    for (a, b) in zip(tab1, tab2):
        if a[-1] == b[-1]:
            odp += 1
    return odp


def parzyste_w_ciag(tablica):
    count = 0
    for i in tablica:
        if i % 2 == 0:
            count += 1
    return count



def zadanie2(tab1, tab2):
    odp = 0
    for (a, b) in zip(tab1, tab2):
        if parzyste_w_ciag(a) == 5 and parzyste_w_ciag(b) == 5:
            odp += 1
    return odp


def porownanie(taba, tabb):
    set_a, set_b = set(taba), set(tabb)
    if set_a == set_b:
        return True
    return False


def zadanie3(tab1, tab2):
    odp = 0
    for (a, b) in zip(tab1, tab2):
        if porownanie(a, b):
            odp += 1
            index = tab1.index(a)
    return odp, index + 1



"""
1, 3, 5, 8
2, 4, 6
1, 2, 3, 4, 5, 6
"""
def scalanie(tab1, tab2):
    tablica = []
    dlg1, dlg2 = len(tab1), len(tab2)
    i, j = 0, 0
    while i < dlg1 and j < dlg2:
        if tab1[i] <= tab2[j]:
            tablica.append(tab1[i])
            i += 1
        else:
            tablica.append(tab2[j])
            j += 1
    if j < dlg2:
        for m in range(j, dlg2):
            tablica.append(tab2[m])
    if i < dlg1:
        for n in range(i, dlg1):
            tablica.append(tab1[n])
    return tablica




def main():
    DANE1, DANE2 = odczyt1('dane1.txt'), odczyt1('dane2.txt')
    # print(DANE1)
    # zad1 = zadanie1(DANE1, DANE2)

    przyklad1 = DANE1[0]
    przyklad2 = DANE2[0]

    # print(zadanie2(DANE1, DANE2))
    # print(zadanie3(DANE1, DANE2))
    print(scalanie([2, 8, 16, 45], [1, 2, 3, 4, 5, 9]))
main()