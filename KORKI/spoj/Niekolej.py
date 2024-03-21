
"""
n -> 0,1,2, ... n

0 1 2 3 4 5
p: 4, 2, 0
Np: 1, 3, 5
0 2 4 1 3 5
"""


n = int(input('n = '))
if n > 3:
    for p in range(0, n + 1, 2):
        print(p)
    for Np in range(1, n + 1, 2):
        print(Np)
elif n == 3:
    print("2 0 3 1")
else:
    print("NIE")