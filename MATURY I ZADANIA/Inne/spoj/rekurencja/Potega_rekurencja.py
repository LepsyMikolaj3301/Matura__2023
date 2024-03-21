"""



"""

def oblicz_pot_iteracyjnie(podstawa: int, wykladnik: int) -> int:
    wynik = 1
    for i in range(wykladnik):
        wynik *= podstawa
    return wynik

def oblicz_pot_rekurencyjnie(podstawa: int, wykladnik: int) -> int:
    if wykladnik == 0:
        return 1
    return podstawa * oblicz_pot_rekurencyjnie(podstawa, wykladnik - 1)

podstawa = int(input('Podstawa: '))
wykladnik = int(input('Wykladnik: '))

print(oblicz_pot_iteracyjnie(podstawa, wykladnik))
print(oblicz_pot_rekurencyjnie(podstawa, wykladnik))
