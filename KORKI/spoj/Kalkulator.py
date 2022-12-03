"""
kalkulator

+ 7 9
wyppluwa: wartość wyrażenia

"""

ile_razy = int(input("Ile razy: "))
for _ in range(ile_razy):
    znak, l1, l2 = input().split()
    l1, l2 = int(l1), int(l2)
    if znak == '+':
        print(l1 + l2)
    elif znak == '-':
        print(l1 - l2)
    elif znak == '*':
        print(l1 * l2)
    elif znak == '/':
        print(int(l1 / l2))
    elif znak == '%':
        print(l1 % l2)
    else: print("ERROR")