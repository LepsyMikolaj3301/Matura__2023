'''


'''


def okr_znaku(liczba: int):
    if liczba == 0:
        return 'zero'
    elif liczba > 0:
        return 'dodatnia'
    else:
        return "ujemna"


def kolejna_pozycja(liczba: list, i = 0):
    if i < len(liczba):
        print(okr_znaku(int(liczba[i])))
        return kolejna_pozycja(liczba, i + 1)


liczby = input().split()
kolejna_pozycja(liczby)
