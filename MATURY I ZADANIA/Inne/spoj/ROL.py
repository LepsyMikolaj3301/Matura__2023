"""
przesuwanie tablicy w lewo


"""


test = int(input())
for _ in range(test):
    dlugosc = int(input())
    table = []
    for l in range(dlugosc):
        table.append(int(input()))
    for i in range(len(table) - 1):
        zmienna_p = table[i]
        table[i] = table[i + 1]
        table[i + 1] = zmienna_p
    print(table)
