"""
SKRÓCONA WERSJA SLOWA: AAA = A3
BAAACCGGGG
1. zapisujemy pierwszy znak
2. porównujemy z następnym
    jeśli taki sam, idziemy dalej z indexem
    póki będzie taki sam, zliczamy wystąpienia
    po jeśli następna inna: Zapisujemy oryginalną literę i liczbe powtórzeń
    ( zliczamy liczby od 0, 1, 2 <= stąd zmieniamy zapis )

        D O    P O P R A W Y ! ! !


ABBCCCDDDDEEEEEFGGHIIJKKKL

KKK LL
KKK KL
KKK KK


"""


def flamaster(slowo_org: str) -> str:
    slowo = slowo_org + ' '
    length = len(slowo)
    after_word = slowo[0]
    counter = 0
    for j in range(1, length):
        char = slowo[j]
        back_char = slowo[j - 1]
        if char == back_char:
            counter += 1
        else:
            if counter > 1:
                after_word += str(counter + 1)
                counter = 0
            elif counter == 1:
                after_word += back_char
                counter = 0
            after_word += char
    after_word = after_word.rstrip(' ')
    return after_word

    # while current_index < length:
    #     after_word += slowo[current_index - 2]
    #     if slowo[current_index - 2] == slowo[current_index] and slowo[current_index - 1] == slowo[current_index]:
    #         current_index += 1
    #         counter = 3
    #         while :
    #             counter += 1
    #             current_index += 1
    #         after_word += str(counter)
    #     else:
    #         current_index += 1


DANE = []
with open("flamaster.txt", 'r') as file:
    for line in file:
        DANE.append(line.rstrip('\n'))
testy = int(DANE[0])
odpowiedzi = []
for i in range(1, testy + 1):
    slowo = DANE[i]
    odpowiedzi.append(flamaster(slowo))
with open("flamaster_o.txt", 'w') as file:
    for slowo in odpowiedzi:
        file.write(slowo + '\n')
