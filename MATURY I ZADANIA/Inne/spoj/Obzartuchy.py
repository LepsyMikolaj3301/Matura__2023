"""
gluttony:
cała doba - non stop ->  24 godziny czyli 86 400 sekund
jedzą ciastka non stop, jeśli je ciastko przy końcu,
nie umie je dokończyć -> zaokrąglamy do całkowitych
stałe tępo obzartucha

wejscie:
    zestawy testowe
    N = liczba obżartuchów, M = ciastka w jednym pudełku
    kolejne N wierszy = czasy w sekundach jedzenia JEDNEGO CIASTKA, jedzenia ciastek

    DO ich czasów TRZEBA TABLIC !!!

rozwiązanie:    dzielimy dobe przez każdy czas -> każde ciastka dla każdego na dobe
                dodajemy wszystkie ciastka uczestników i zaokrąglamy dla wielkości pudełka
                le go

"""

tries = int(input("Proby: "))
for _ in range(tries):
    gluttons_num, sizing_pudlo = input('N, M = ').split()
    gluttons_num, sizing_pudlo = int(gluttons_num), int(sizing_pudlo)
    doba = 86400
    ciastka_na_dob = 0
    for i in range(gluttons_num):
        czas = int(input())
        ciastka_na_dob += doba // czas
    if ciastka_na_dob % sizing_pudlo > 0:
        print(ciastka_na_dob // sizing_pudlo + 1)
    else:
        print(ciastka_na_dob // sizing_pudlo)
