"""



"""
def selection_sort(tablica: list):
    for n in range(len(tablica) - 1):
        najmn_index = n
        for i in tablica[n + 1:]:
            if i < tablica[najmn_index]:
                 = i
        tablica[n], tablica[najmn_index] = tablica[najmn_index], tablica[n]
    return tablica



lista = [int(i) for i in "2,3,4,63,434,2,43,1,9".split(',')]
print(lista)
print(selection_sort(tablica=lista))
