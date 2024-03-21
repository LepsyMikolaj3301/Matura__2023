"""
Liczba pierwsza to taka liczba naturalna większa od 1,
której jedynymi naturalnymi dzielnikami jest liczba 1 i ona sama.


x ** 0.5 <- pierwiastek z n

"""


def liczba_pierwsza(liczba: int):
    if liczba < 2:
        return False
    for i in range(2, liczba):
        if liczba % i == 0:
            return False
    return True


if __name__ == '__main__':
    num = 15
    print(liczba_pierwsza(num))
