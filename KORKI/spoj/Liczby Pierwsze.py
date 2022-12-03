"""
Liczby pierwsze


"""

n = int(input("Testy: "))
for _ in range(n):
    liczba = int(input("liczba: "))
    for i in range(2, liczba):
        if liczba % i == 0:
            print("NIE")
            break
        print("TAK")
