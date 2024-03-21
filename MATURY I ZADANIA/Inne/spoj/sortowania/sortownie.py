"""
1, 3, 2, 8, 7, 4
4, 5, 6, 12, 18, 1 
4

sortowanie bąbelkowe działanie:

13, 30, 56, 6, 10, 120
13
13, 30
13, 30, 56,
13, 30, 56, 6
13, 30, 6, 56
13, 6, 30, 56
6, 13, 30, 56
1 { 3, 2, 4, 7, 8

"""


def index_najm_wartosc(lista: list, current_index: int) -> int:
    index_min = current_index
    for y in range(current_index + 1, len(lista)):
        if lista[index_min] > lista[y]:
            index_min = y
    return index_min


def sortowanie_wybieranie(tablica: list):
    for i in range(len(tablica)):
        index_najmniejsza = index_najm_wartosc(tablica, i)
        tablica[index_najmniejsza], tablica[i] = tablica[i], tablica[index_najmniejsza]
    return tablica


def sortowanie_babelkowe(tablica: list):
    for i in range(len(tablica)):
        for j in range(len(tablica) - 1):
            if tablica[j] > tablica[j + 1]:
                tablica[j], tablica[j + 1] = tablica[j + 1], tablica[j]
    return tablica


def sortowanie_wstawianie(tablica: list):
    for i in range(1, len(tablica)):
        j = i
        while j > 0 and tablica[j - 1] > tablica[j]:
            tablica[j], tablica[j - 1] = tablica[j - 1], tablica[j]
            j -= 1
    return tablica


lista = [1, 3, 5, 6, 9, 12, 8, 90, 123, 80, 30]
print(sortowanie_wstawianie(lista))
