"""
5 3
1 2 3 4 5

"""
test = int(input())
for _ in range(test):
    dlugosc, k_miejsc = int(input("d:")), int(input("k:"))
    table = []
    for l in range(dlugosc):
        table.append(int(input()))

    table_p = table[0:k_miejsc]
    for i in range(k_miejsc):
        table.pop(0)
    table.extend(table_p)

    # for i in range(len(table) - k_miejsc):
    #     zmienna_p = table[i]
    #     table[i] = table[i + k_miejsc]
    #     table[i + k_miejsc] = zmienna_p
    print(table)

