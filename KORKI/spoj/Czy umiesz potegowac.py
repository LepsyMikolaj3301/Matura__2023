"""
czy umiesz potegowac:
a ^ b = a * a * ... b times
podajemy a oraz b
"""
tests = int(input("Ilosc prob: "))
for _ in range(tests):
    a, b = input().split()
    a = int(a)
    b = int(b)
    wynik = a
    for _ in range(b - 1):
        wynik *= a
    print(wynik % 10)
