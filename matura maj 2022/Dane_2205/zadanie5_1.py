"""
E:\\Matura__2023\\matura maj 2022\\Dane_2205\\liczby.txt
"""


def opening() -> tuple:
    table = []
    with open("E:\\Matura__2023\\matura maj 2022\\Dane_2205\\liczby.txt", 'r') as file:
        for line in file:
            table.append(line[0:-1])
    return tuple(table)

# checking dla liczby, która na końcach ma liczby które się równają
def checking_bruh(num: str) -> bool:
    for i in range(1, (int(len(num)/2)) + 1):
        if num[0:i] == num[-i:]:
            return True
    else:
        return False
#dobre checking
def checking(num: str) -> bool:
    if num[0] == num[-1]:
        return True
    return False

def zadanie_5_1(numbers: tuple):
    the_chosen = []
    how_much = 0
    for number in numbers:
        if checking(number):
            the_chosen.append(number)
    return the_chosen


liczby = zadanie_5_1(opening())
print(liczby)
print(len(liczby), liczby[0])
