"""
(2*(v1*v2))/(v1+v2)
2 * 60 * 40 / 100  = 4800 / 100


"""

with open("spoj_dane\\pr_sr.txt") as file:
    DANE_ALL = []
    for line in file:
        DANE_ALL.append(line)
testy = int(DANE_ALL[0])
odpowiedzi = []
for i in range(testy):
    v1, v2 = DANE_ALL[i + 1].split()
    v1, v2 = int(v1), int(v2)
    prdk_srd = str(2 * (v1 * v2) // (v1 + v2))
    odpowiedzi.append(prdk_srd)
with open("spoj_odpowiedzi\\pr_sr_o.txt", 'w') as file:
    for i in odpowiedzi:
        file.write(i + '\n')
