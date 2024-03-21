<<<<<<< HEAD
"""
https://pl.spoj.com/problems/KC004/

homework ( tylko fory, ify, zmienne )

ID:
438
496
499
522
601
626
804
968
997 +
1032
1042
1211 +
1102
"""

wartosc = int(input("Ile razy? "))

for i in range(wartosc):
    rozw = 0
    num_searched = int(input("liczba: "))
    how_long = int(input("dlugosc: "))
    for num in range(how_long):
        num_given = int(input("liczba podawana: "))
        if num_given == num_searched:
            rozw += 1
    print(rozw)

