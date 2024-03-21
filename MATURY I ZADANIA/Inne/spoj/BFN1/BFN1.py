"""
robienie liczby aż bedzie palindromem

liczba = 28

sprawdzanie czy to palindrom
jeśli nie:
28 + 82 = 110
repeat

"""


def zamien_int_na_str(liczba: int) -> str:
    x = 10
    liczba_str = ""
    while liczba > 0:
        liczba_str = chr((liczba % x) + 48) + liczba_str
        liczba //= x
    return liczba_str


def zamien_str_na_int(liczba: str) -> int:
    liczba_int = 0
    length = len(liczba)
    for j in range(length):
        liczba_int += (ord(liczba[j]) - 48) * (10 ** (length - j - 1))
    return liczba_int

def zamiana_kolej(word: str) -> str:
    word_p = ''
    for i in word:
        word_p = i + word_p
    return word_p

def czy_palindrom(word: str, word_p: str) -> bool:
    if word == word_p:
        return True
    else:
        return False

def sprawdzanie_liczby(liczba: str):
    times = 0
    while True:
        if czy_palindrom(liczba, zamiana_kolej(liczba)):
            break
        else:
            liczba = zamien_int_na_str(zamien_str_na_int(liczba) + zamien_str_na_int(zamiana_kolej(liczba)))
            times += 1
    return liczba, times

def main():
    DANE = []
    with open("BFN1.txt", 'r') as file:
        for line in file:
            DANE.append(line.rstrip('\n'))
    proby = DANE[0]
    for i in range(zamien_str_na_int(proby)):
        number = DANE[i + 1]
        palindrom_number, times = sprawdzanie_liczby(number)
        print(palindrom_number, times)


main()