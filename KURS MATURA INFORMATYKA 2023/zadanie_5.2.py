"""
Napisz program sumujący elementy parzyste i nieparzyste - tablicy dwuwymiarowej.
"""

tablica = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]


def zadanie_5_2(tablic_dwuw: list) -> tuple:
    suma_parz, suma_nieparz = 0, 0
    for lista in tablic_dwuw:
        for wartosc in lista:
            if wartosc % 2 == 0:
                suma_parz += wartosc
            else:
                suma_nieparz += wartosc
    odpowiedzi = (suma_parz, suma_nieparz)
    return odpowiedzi


print(zadanie_5_2(tablica))
