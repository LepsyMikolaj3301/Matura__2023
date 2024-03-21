"""



"""


def luka(x_pop: int, x: int):
    r = abs(x - x_pop)
    return r

def zadanie1(tablica: list):
    najwieksza, najmniejsza = tablica[0], tablica[0]
    for index in range(1, len(tablica)):
        luken = luka(tablica[index - 1], tablica[index])
        if luken > najwieksza:
            najwieksza = luken
        elif luken < najmniejsza:
            najmniejsza = luken
        else:
            continue
    return najwieksza, najmniejsza

# [4, 11, 4, 1, 4, 7, 11, 12, 13, 14, 7, 0, 3]

def zadanie2(tablica):
    odp_index, odp_long = 0, 1
    longen = 2
    r_test = luka(tablica[0], tablica[1])
    for i in range(1, len(tablica)):
        r = luka(tablica[i - 1], tablica[i])
        if r != r_test:
            if longen > odp_long:
                odp_index = i - longen
                odp_long = longen
                last = tablica[i - 1]
            longen = 2
        else:
            longen += 1
        r_test = r

    first = tablica[odp_index]
    return first, last, odp_long


def main():
    DANE = []
    with open("DANE_PR\\dane4.txt", 'r') as file:
        for line in file:
            DANE.append(int(line.rstrip('\n')))
    tab = [4, 11, 4, 1, 4, 7, 11, 12, 13, 14, 7, 0, 3]
    print(zadanie2(tab))

    # print(DANE)
    # maxim, minim = zadanie1(DANE)
    # print(f'Maximum: {maxim}, minimum: {minim}')


main()
