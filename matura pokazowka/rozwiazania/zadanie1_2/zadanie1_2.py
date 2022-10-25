import os
import sys

def fileAsListOfstr() -> list:
    theGame = []
    with open(os.path.join(sys.path[0],'szachy.txt'), 'r') as file:
        for line in file:
            theGame.append(line[0:8])
    return theGame



def zadanie1_2(chessGame: list) -> list:

    #zmienne 0 - plansz z równowagą;  1 - najmniejsza liczba bierek len(whitePieces)
    stalePosition = 0
    theLiestBierkiOfSide = 18
    blackPieces, whitePieces = [], []
    for line in chessGame:
        if line == '\n':
            if len(whitePieces) == len(blackPieces):
                whitePieces.sort()
                blackPieces.sort()
                for i, j in enumerate(whitePieces):
                    SimilarPiece = blackPieces[i].upper()
                    if j != SimilarPiece:
                        break
                else:
                    stalePosition += 1
                    if theLiestBierkiOfSide > len(whitePieces):
                        theLiestBierkiOfSide = len(whitePieces)
            #clearing
            blackPieces.clear()
            whitePieces.clear()
            continue
        for place in line:
            if place != '.':
                if place.isupper():
                    whitePieces.append(place)
                elif place.islower():
                    blackPieces.append(place)

    return stalePosition, theLiestBierkiOfSide * 2


stalePositions, LiestBierkiNum = zadanie1_2(fileAsListOfstr())
print(stalePositions, LiestBierkiNum)

# print( fileAsListOfstr())
