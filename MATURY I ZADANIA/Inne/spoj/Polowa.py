"""
liczba całkowita t
podzielne na połowe 2k
...

"""


DANE = []
with open("spoj_dane\\po.txt", 'r') as file:
    for line in file:
        DANE.append(line)
testy = int(DANE[0])
odpowiedzi = []
for i in range(testy):
    wyraz = DANE[i + 1]
    pol_wyr = ""
    for n in range(len(wyraz) // 2):
        pol_wyr += wyraz[n]
    odpowiedzi.append(pol_wyr)
with open("spoj_odpowiedzi\\po_o.txt", 'w') as file:
    for i in odpowiedzi:
        file.write(i + '\n')