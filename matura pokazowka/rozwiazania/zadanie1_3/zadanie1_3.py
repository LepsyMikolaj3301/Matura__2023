from audioop import bias
import os
import sys

'''
game = fileAsListOfstr()
print(game)

for i in range(72):
    if i % 8 == 0:
        print(game[i])




'''

def fileAsListOfstr() -> list:
    # PATHING = 'E:\\Rep__python\\MATURA 2023\\matura pokazowka\\rozwiazania\\zadanie1_3\\'
    theGame = []
    with open('E:\\Rep__python\\MATURA 2023\\matura pokazowka\\rozwiazania\\zadanie1_3\\szachy.txt', 'r') as file:
        for line in file:
            theGame.append(line.rstrip('\n'))
        for line in theGame:
            if line == '':
                theGame.remove(line)
    return theGame

def changingListOfLinesIntoColumns(linesList: list) -> list:
    listOfColumns = [[] for _ in range(8)]
    for index, value in enumerate(linesList):
        listOfColumns[index].append(value)
    return listOfColumns

# to zmień na dole

def checkingKropa(line: str) -> bool:
    twoLetters = 0
    for i in line:
        if i.isalpha():
            twoLetters += 1
    if twoLetters == 2: return True
    else: return False

def checkingIfSzach(currentBoard: list) -> tuple:
    blackSzach, whiteSzach = 0, 0
    for line in currentBoard:

        # ZRÓB STATEMENT
        
        if 'k' in line and 'W' in line and not line[line.index('k'): line.index('W')].isalpha():
            whiteSzach += 1
        if 'K' in line and 'w' in line and not line[line.index('K'): line.index('w')].isalpha():
            blackSzach += 1
    return whiteSzach, blackSzach

def zadanie1_3(chessGame: list) -> tuple:
    #zmienne:
    WszachB, BszachW = 0, 0
    answer1 = 0
    answer2 = 0
    tempChessPosition = []
    
    for index, line in enumerate(chessGame):
        if index % 8 == 0:
            WszachB, BszachW = checkingIfSzach(tempChessPosition)
            answer1 += WszachB
            answer2 += BszachW
            WszachB, BszachW = checkingIfSzach(changingListOfLinesIntoColumns(tempChessPosition))
            answer1 += WszachB
            answer2 += BszachW
            # clearing
            tempChessPosition.clear()
        tempChessPosition.append(line)

    return answer1, answer2

BialeSzachujo, CzarneSzachujo = zadanie1_3(fileAsListOfstr())
print(BialeSzachujo, CzarneSzachujo)




