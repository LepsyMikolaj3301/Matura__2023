'''
funkcja przyjmuje dowolną liczbę i zwraca jako string

str() -> nie korzystamy

liczba = 123
tab = [1, 2, 3]
chr( tab[i] + 48 )
'3' , 23
123 % 10 = 3
12 % 10 = 2
1 % 10 = 1


'123'

'''


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

print(zamien_int_na_str(0))