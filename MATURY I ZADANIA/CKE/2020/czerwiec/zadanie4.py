"""
pary i przykład tak o


"""


def sito(n):
    bools = [True for _ in range(n)]
    primes = []
    for i in range(len(bools)):
        if i <= 1:
            bools[i] = False
        else:
            if bools[i]:
                primes.append(i)
                for j in range(i, len(bools), i):
                    bools[j] = False
    return primes




def mhg(liczba: int):
    primersy = sito(liczba)
    for i in range(len(primersy)):
        for j in range(len(primersy) - 1, i - 1, -1):
            a, b = primersy[i], primersy[j]
            if a + b == liczba:
                return a, b


def zadanie1(tablica):
    tab_of_nums = [tablica[i][0] for i in range(len(tablica))]
    with open("odpowiedzi\\odpowiedzi.txt", 'a') as f:
        f.write(f"4.1: \n")
        for num in tab_of_nums:
            if num % 2 == 0:
                nums_of_mhg = mhg(num)
                if nums_of_mhg:
                    print(num, nums_of_mhg)
                    f.write(f"{num} {nums_of_mhg[0]} {nums_of_mhg[1]}")
    return


def long_of_ciag(ciag):
    longest_repeat = 1
    letter_of_longest = ciag[0]
    repeats = 1
    for i in range(1, len(ciag)):
        if ciag[i - 1] != ciag[i]:
            repeats = 1
        else:
            repeats += 1
        if repeats > longest_repeat:
            longest_repeat = repeats
            letter_of_longest = ciag[i - 1]
    return letter_of_longest * longest_repeat, longest_repeat


def zadanie2(tablica):
    tab_of_ciag = [tablica[i][1] for i in range(len(tablica))]
    for ciag in tab_of_ciag:
        l_ciag, rep = long_of_ciag(ciag)
        print(f"{l_ciag} {rep}")


def zadanie3(tablica):


def main():
    DANE = []
    with open("Dane_PR2\\przyklad.txt", 'r') as file:
        for line in file:
            liw = line.split()
            DANE.append([int(liw[0]), liw[1]])
    zadanie1(DANE)
    zadanie2(DANE)


main()
