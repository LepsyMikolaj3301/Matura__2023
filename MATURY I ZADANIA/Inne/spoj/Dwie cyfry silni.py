"""
silnia
n = 1*2*3*...*n,
1. ile prób

"""

tests = int(input("Ilosc prob: "))

for _ in range(tests):
    liczba = 1
    n = int(input("n = "))
    for num in range(n):
        liczba *= num + 1
    jedn = liczba % 10
    print("liczba dzies: ", int((liczba % 100 - jedn)/10), " liczba jednosci: ", jedn)
