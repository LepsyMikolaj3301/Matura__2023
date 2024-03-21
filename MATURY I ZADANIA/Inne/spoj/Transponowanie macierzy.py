"""
transponowanie macierzy <-> jej obrót w taki sposób, że

    jej kolumny staną się wierszami, a wiersze - kolumnami

1 2 5                       1 4 3 8
4 3 3                       2 3 4 7
3 4 9                       5 3 9 7
8 7 7


"""

x, y = input().split()
x, y = int(x), int(y)
matrix = []
for _ in range(x):
    matrix.append(list(input().split()))

for i in matrix:
    for j in i:
        j = int(j)

for i in range(y):
    for j in range(x):
        print(matrix[j][i], end=' ')
    print()

# aby zrobić transponacje, wystarczy zamiast printa, przypisać do nowego matrixa

