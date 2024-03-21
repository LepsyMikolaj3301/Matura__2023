"""
2 grupy przedszkolaków
dzielimy równo, po obu grupach z osobna
liczba cukierków % ilość przedszkolaków = 0
ona dostaje tylko jedną grupe do zasłodzenia

NWW czyli najmniejsza wspólna wielokrotność

"""

testy = int(input("Ilosc test: "))
for _ in range(testy):
    a, b = input().split()
    a, b = int(a), int(b)
    nww = 1
    if a > b:
        bigger_num = a
    else:
        bigger_num = b
    i = 2
    while bigger_num >= i:
        if a % i == 0 or b % i == 0:
            if a % i == 0:
                a = int(a / i)
            if b % i == 0:
                b = int(b / i)
            nww *= i
        else:
            if a == 1 and b == 1:
                break
            i += 1
    print(nww)

