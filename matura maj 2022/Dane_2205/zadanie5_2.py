"""
E:\\Matura__2023\\matura maj 2022\\Dane_2205\\liczby.txt
"""


def opening() -> tuple:
    table = []
    with open("E:\\Matura__2023\\matura maj 2022\\Dane_2205\\przyklad.txt", 'r') as file:
        for line in file:
            table.append(line[0:-1])
    return tuple(table)

def zadanie_5_2(numbers: tuple) -> list:
    