"""



"""


def odczyt1():
    dane1 = []
    with open("NM_DANE_PR\\przyklad1.txt", 'r') as file1:
        for line in file1:
            dane1.append(line.rstrip('\n').split())
    return dane1


def odczyt2():
    dane2 = []
    with open("NM_DANE_PR\\przyklad2.txt", 'r') as file1:
        for line in file1:
            dane2.append(line.rstrip('\n').split())
    return dane2


def parzyste_numy(table):
    odp = 0
    for i in table:
        if int(i) % 2 == 0:
            odp += 1
    if odp == 5:
        return True
    return False


def zadanie4_2(tab1, tab2):
    odp = 0
    for (a, b) in zip(tab1, tab2):
        if parzyste_numy(a) and parzyste_numy(b):
            odp += 1
    return odp


def zadanie4_1(tab1, tab2):
    # for (a, b) in zip(tab1, tab2):
    odp = 0
    for i in range(len(tab1)):
        if tab1[i][-1] == tab2[i][-1]:
            odp += 1
    return odp


def zadanie4_3(tab1, tab2):
    odpowiedzi = []
    for j, (a, b) in enumerate(zip(tab1, tab2)):
        if set(a) == set(b):
            odpowiedzi.append(j + 1)
    return odpowiedzi, len(odpowiedzi)


def zadanie4_4_nielegalne_rozwiazanie(tab1, tab2):
    new_list = []
    for i in range(len(tab1)):
        list_c = tab1[i]
        list_c.extend(tab2[i])
        for j, i in enumerate(list_c):
            list_c[j] = int(i)
        list_c.sort()
        new_list.append(list_c)
    return new_list




"""
1 2 3 4
5 6 7 8
1 2 3 4

or 0, 1 => 1
0, 1 -> 0
"""


def scalanie(a, b):
    c = []
    i, j = 0, 0
    while i < len(a) and j < len(b):
        while i < len(a) and int(a[i]) <= int(b[j]):
            c.append(int(a[i]))
            if i < 10:
                i += 1
        while j < len(b) and i < 10 and int(b[j]) < int(a[i]):
            c.append(int(b[j]))
            if j < 10:
                j += 1
    if i > j:
        for n in range(j, len(b)):
            c.append(int(b[n]))
    elif i < j:
        for m in range(i, len(a)):
            c.append(int(a[m]))
    return c
# ?


def zadanie4_4_legalne(tab1, tab2):
    with open("odpowiedzi\\wyniki4_4.txt", 'w') as file:
        for (a, b) in zip(tab1, tab2):
            new_ciag = scalanie(a, b)
            for i in new_ciag:
                file.write(str(i) + ' ')
            file.write('\n')
    return


def main():
    DANE1 = odczyt1()
    DANE2 = odczyt2()
    print(scalanie(DANE1[0], DANE2[0]))
    zadanie4_4_legalne(DANE1, DANE2)
main()
