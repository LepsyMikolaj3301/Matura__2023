"""
lista liter jest wypluwana, wraz z ilością w CAłYM ZAPISIE

A -> Z | a -> z
65 -> 90 i 97 -> 122

"""
# ord( string ) => liczba w kodzie ASCII
# chr( liczba ) => litera w kodzie ASCII
DANE = []
with open("spoj_dane\\zl_li.txt", 'r') as file:
    for line in file:
        DANE.append(line)
testy = int(DANE[0])
zdania = ""
for i in range(testy):
    zdania += DANE[i + 1]
with open("spoj_odpowiedzi\\zl_li_o.txt", 'w') as file:
    for kod in range(ord('a'), ord('z')):
        lit_asci = chr(kod)
        licznik = 0
        for litera in zdania:
            if litera == lit_asci:
                licznik += 1
        if licznik > 0:
            file.write(lit_asci + ' ' + str(licznik) + '\n')
    for kod in range(ord('A'), ord('Z')):
        lit_asci = chr(kod)
        licznik = 0
        for litera in zdania:
            if litera == lit_asci:
                licznik += 1
        if licznik > 0:
            file.write(lit_asci + ' ' + str(licznik) + '\n')