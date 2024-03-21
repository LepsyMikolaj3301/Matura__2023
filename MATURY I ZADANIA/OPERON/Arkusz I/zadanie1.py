"""



"""

def liczby_szczesliwe():
    liczby = [True for _ in range(1001)]
    for i in range(2, 1001, 2):
        liczby[i] = False
    liczby[0] = False
    for index, j in enumerate(liczby):
        if j and index != 1:
            for n in range(index, 1001, index):
                liczby[n] = False
    liczby_szcz = []
    for ind, m in enumerate(liczby):
        if m:
            liczby_szcz.append(ind)
    return liczby_szcz



def main():
    print(liczby_szczesliwe())



main()