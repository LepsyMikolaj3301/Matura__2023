"""
funkcja zamieniająca dowolną liczbe na inny system

2 wartości
1. liczba w systemie dziesiętnym
2. podstawa systemu na który chcemy zamienić

od 2 do 16 podstawy

na dwójkowy
12 % 2



"""

def zamien_int_na_str(liczba: int) -> str:
    x = 10
    liczba_str = ""
    if liczba == 0:
        return '0'
    while liczba != 0:
        liczba_str = chr((liczba % x) + 48) + liczba_str
        liczba //= x

    return liczba_str


def zamien_str_na_int(liczba: str) -> int:
    liczba_int = 0
    length = len(liczba)
    for j in range(length):
        liczba_int += (ord(liczba[j]) - 48) * (10 ** (length - j - 1))
    return liczba_int


def cyfry_systemow_wyzszych(cyfra: int) -> str:
    znak = chr(cyfra + 55)
    return znak


def konwertuj_z_10_na_dowolny(liczba: int, system: int) -> str:
    liczba_po_zam = ''
    while liczba > 0:
        reszta = liczba % system
        if reszta > 10:
            liczba_po_zam = cyfry_systemow_wyzszych(reszta) + liczba_po_zam
        else:
            liczba_po_zam = zamien_int_na_str(reszta) + liczba_po_zam
        liczba //= system
    return liczba_po_zam


def znaki_wyższe_na_10(znak) -> int:
    if ord(znak) > 64:
        return ord(znak) - 55
    else:
        return zamien_str_na_int(znak)


def konwertuj_z_dowolnego_na_10(liczba: str, system: int) -> int:
    liczba_po_zam = 0
    power = len(liczba)
    for znak in liczba:
        cyfra = znaki_wyższe_na_10(znak)
        liczba_po_zam += cyfra * (system ** (power - 1))
        power -= 1
    return liczba_po_zam


print(konwertuj_z_dowolnego_na_10('7B', 16))
