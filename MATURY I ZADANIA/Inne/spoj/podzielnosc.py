"""
podzielnosc:
Wypisz wszystkie liczby ai podzielne przez x
i niepodzielne przez y, gdzie 1 < ai < n < 100000.

n x y
n - do jakiej liczby
x - podzielne przez x
y - niepodzielne przez y
"""


tries = int(input("Proby: "))
for _ in range(tries):
    n, x, y = input().split()
    n, x, y = int(n), int(x), int(y)
    for i in range(1, n):
        if i % x == 0 and i % y != 0:
            print(i)
