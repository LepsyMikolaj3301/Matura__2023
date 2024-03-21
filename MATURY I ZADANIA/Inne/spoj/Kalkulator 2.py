"""
Przyjmujemy, że nasz kalkulator ma w pamięci 10 rejestrów o numerach 0 - 9

"""

table = []
for _ in range(10):
    table.append(0)

while True:
    znak, a, b = input().split()
    a, b = int(a), int(b)
    if znak == 'z':
        table[a] = b
    elif znak == '+':
        print(table[a] + table[b])
    elif znak == '-':
        print(table[a] - table[b])
    elif znak == '*':
        print(table[a] * table[b])
    elif znak == '/':
        print(table[a] // table[b])
    elif znak == '%':
        print(table[a] % table[b])
