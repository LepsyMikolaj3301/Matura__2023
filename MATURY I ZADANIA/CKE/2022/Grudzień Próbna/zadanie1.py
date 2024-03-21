"""



"""


def zadanie1(mecz):
    print(len(mecz))
    odpowiedz = 0
    for i in range(len(mecz) - 1):
        if mecz[i] != mecz[i + 1]:
            odpowiedz += 1
    return odpowiedz

def zadanie2(mecz):
    licz_a, licz_b = 0, 0
    for wynik in mecz:
        if licz_a >= 1000 or licz_b >= 1000:
            if abs(licz_a - licz_b) >= 3:
                if licz_a > licz_b:
                    return ["A", licz_a, licz_b]
                else:
                    return ["B", licz_a, licz_b]
        if wynik == "A":
            licz_a += 1
        else:
            licz_b += 1



def main():
    DANE = ""
    with open("Dane_2212\\mecz.txt", 'r') as f:
        DANE = f.read()
        DANE.rstrip()
    print(zadanie1(DANE))
    print(zadanie2(DANE))
main()