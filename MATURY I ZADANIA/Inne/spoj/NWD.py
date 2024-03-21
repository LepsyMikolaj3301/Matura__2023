"""
napisz funkcję NWD
NWD - największy wspólny dzielnik

"""


def nwd(a: int, b: int) -> int:
    if a < b:
        nwd = a
    else:
        nwd = b
    while a % nwd != 0 or b % nwd != 0:
        nwd -= 1
    return nwd


tries = int(input("Proby: "))
for _ in range(tries):
    num1, num2 = input().split()
    num1, num2 = int(num1), int(num2)
    print(nwd(num1, num2))
