"""
2
1 2 3 4 5 6 7 8 9
index_l = 0
index_p = 8
sr = 0 + 8 // 2  = 4

tab[4] ? 2

> => 1 2 3 4
< => 6 7 8 9

divide and conquer

"""


def wyszukiwanie_binarnie(tab_sorted: list, szukana: int) -> int:
    # szukamy indexu gdzie znajduje się dana liczba ( czyli .index() )
    index_l, index_p = 0, len(tab_sorted) - 1

    while index_l <= index_p:
        index_sr = (index_l + index_l) // 2

        if tab_sorted[index_sr] != szukana:
            if tab_sorted[index_sr] > szukana:
                index_p = index_sr - 1
            else:
                index_l = index_sr + 1
        else:
            return index_sr
    else:
        return None


lista = [int(i) for i in "1 2 3 4 5 6 7 8 9 10".split()]
print(lista)
print(wyszukiwanie_binarnie(lista, 7))
