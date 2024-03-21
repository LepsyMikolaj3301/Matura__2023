"""
16331 7


"""

def zadanie1(tablica):
    with open("odpowiedzi\\wyniki_6_1.txt", 'w') as file:
        liczba_osiem = 0
        for i in tablica:
            if i[-1] == '8':
                liczba_osiem += 1
        print('zadanie1: ' , liczba_osiem)
        file.write(str(liczba_osiem))

def zadanie2(tablica):
    with open("odpowiedzi\\wyniki_6_2.txt", 'w') as file:
        odpowiedz = 0
        for line in tablica:
            if line[-1] == '4':
                if '0' not in line:
                    odpowiedz += 1
        print('zadanie 2: ' , odpowiedz)
        file.write(str(odpowiedz))

def zadanie3(tablica):
    with open("odpowiedzi\\wyniki_6_3.txt", 'w') as file:
        odpowiedz = 0
        for lin in tablica:
            if lin[-1] == '2':
                if lin[-2] == '0':
                    odpowiedz += 1
        print('Zadanie 3: ' , odpowiedz)
        file.write(str(odpowiedz))

def zamiana_na_base_ten(system_origin: int, num: str):
    num_inverse = list(num[::-1])
    base_10 = 0
    for index, value in enumerate(num_inverse):
        base_10 += int(value) * (system_origin ** index)
    return base_10



def zadanie4(tablica):
    with open("odpowiedzi\\wyniki_6_4.txt", 'w') as file:
        odpowiedz = 0
        for line in tablica:
            if line[-1] == "8":
                base = int(line[-1])
                liczba_in_str = line[:-1]
                odpowiedz += zamiana_na_base_ten(base, liczba_in_str)
        print('Zadanie4: ', odpowiedz)
        file.write(str(odpowiedz))



def zadanie5(tablica):
    with open("odpowiedzi\\wyniki_6_5.txt", 'w') as file:
        first_line = tablica[0]
        minimumen = [first_line, zamiana_na_base_ten(int(first_line[-1]), first_line[:-1])]
        maximunen = [first_line, zamiana_na_base_ten(int(first_line[-1]), first_line[:-1])]
        for line in tablica[1:]:
            base = int(line[-1])
            liczba_in_str = line[:-1]
            value_of_kod = zamiana_na_base_ten(base, liczba_in_str)
            if value_of_kod > maximunen[1]:
                maximunen[0], maximunen[1] = line, value_of_kod
            if value_of_kod < minimumen[1]:
                minimumen[0], minimumen[1] = line, value_of_kod
        file.write("Najwieksza: " + maximunen[0] + '\n' + "Wartosc dziesietna: " + str(maximunen[1]) + '\n')
        file.write("Najmniejsza: " + minimumen[0] + '\n' + "Wartosc dziesietna: " + str(minimumen[1]))

def main():
    DANE = []
    with open("MIN-R2A1P-163_dane\\liczby.txt", 'r') as f:
        for line in f:
            DANE.append(line.rstrip('\n'))
    zadanie1(DANE)
    zadanie2(DANE)
    zadanie3(DANE)
    zadanie4(DANE)
    zadanie5(DANE)

main()
