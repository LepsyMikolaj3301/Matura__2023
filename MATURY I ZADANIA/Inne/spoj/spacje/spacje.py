"""
usuwanie spacji i następna litera ma być z dużej


duża litera jest zawsze 32 miejsca dalej

funkcje ascii:
chr(int)
ord('string')
"""

DANE = []
with open('spacje.txt', 'r') as file:
    for line in file:
        DANE.append(line.rstrip('\n'))
with open('spacje_o.txt', 'w') as file:
    for zdanie in DANE:
        nowe_zdanie = ''
        nastepny_upper = 'False'
        for i in zdanie:
            if i == ' ':
                nastepny_upper = 'True'
                continue
            else:
                if nastepny_upper:
                    nowe_zdanie += i.upper()
                    nastepny_upper = not nastepny_upper
                else:
                    nowe_zdanie += i
        file.write(nowe_zdanie + '\n')

