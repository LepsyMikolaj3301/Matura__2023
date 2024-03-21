"""
th 3x + 1 problem

x0=s,
xn+1=3*xn+1, jeśli xn jest nieparzyste i
xn+1=xn/2, jeśli xn jest parzyste

"""


def collatz(number_s: int, n: int) -> int:
    if number_s != 1:
        if number_s % 2 == 0:
            return collatz(number_s // 2, n + 1)
        else:
            return collatz(3 * number_s + 1, n + 1)
    else:
        return n


while True:
    number = int(input("number_s ( 0 kończy program ): "))
    if number != 0:
        odpowiedz = collatz(number, 0)
        print(odpowiedz)
    else:
        break
