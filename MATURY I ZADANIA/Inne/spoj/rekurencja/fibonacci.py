"""
Ciąg fibonacci => a,b
c = a + b
d = c + b
...
"""

def fibonacci_iteracyjnie(numer_elementu:int):

    tab = [0, 1]
    for i in range(2, numer_elementu):
        tab.append(tab[i - 2] + tab[i - 1])
    return tab[numer_elementu - 1]

def fibonacci_rekurencyjnie(numer_elementu:int):
    if numer_elementu == 1:
        return 0
    if numer_elementu == 2:
        return 1
    return fibonacci_rekurencyjnie(numer_elementu - 2) + fibonacci_rekurencyjnie(numer_elementu - 1)


print(fibonacci_iteracyjnie(1))
print(fibonacci_rekurencyjnie(5))
