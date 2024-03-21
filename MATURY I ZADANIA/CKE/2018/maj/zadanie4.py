"""



"""


def odczyt():
    dane = []
    with open("Dane_PR\\sygnaly.txt", 'r') as file:
        for i in file:
            dane.append(i.rstrip('\n'))
    return dane


def zadanie4_1(tablica):
    odpowiedz = ""
    for i in range(40, 1001, 40):
        odpowiedz += tablica[i - 1][9]
    return odpowiedz


def zadanie4_2(tablica):
    biggest_set = set(tablica[0])
    word = tablica[0]
    for i in tablica:
        if len(set(i)) > len(biggest_set):
            biggest_set = set(i)
            word = i
    return biggest_set, word


def porownanie(char1, char2):
    if abs(ord(char1) - ord(char2)) <= 10:
        return True
    return False


def zadanie4_3(tablica):
    odpowiedzi = []
    for word in tablica:
        set_of_line = list(set(word))
        good = True
        for i in range(len(set_of_line)):
            for j in range(i + 1, len(set_of_line)):
                if not porownanie(set_of_line[i], set_of_line[j]):
                    good = False
            if not good:
                break
        if good:
            odpowiedzi.append(word)
    return odpowiedzi


def main():
    DANE = odczyt()
    print(zadanie4_1(DANE))
    # print(zadanie4_3(DANE))
    with open("odpowiedzi\\wyniki4.txt", 'w') as f:
        f.write(f"4.1 {zadanie4_1(DANE)}\n")
        setofword, word = zadanie4_2(DANE)
        f.write(f"4.2 {str(word)} {len(setofword)}")
        f.write('\n4.3 \n')
        answer = zadanie4_3(DANE)
        for i in answer:
            f.write(str(i) + '\n')


main()