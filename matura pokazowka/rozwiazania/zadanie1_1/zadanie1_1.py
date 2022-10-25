import os
import sys as sus

def fileAsListOfstr() -> list:
    theGame = []
    with open(os.path.join(sus.path[0],'szachy.txt'), 'r') as file:
        for line in file:
            theGame.append(line.strip('\n'))
    for line in theGame:
        if line == '':
            theGame.remove(line)
    return theGame


def MostCCPositionCheck(columnNumber, MostCCinPosition: int) -> int:
    if columnNumber > MostCCinPosition:
        MostCCinPosition = columnNumber
    return MostCCinPosition
    


def theLogic_column(chessGame: list) -> list:
    # CC => Clear Columns
    numOfCCPositions = 0
    tempMostPositions = 0
    MostCCinPosition = 0
    listOfColumns = [[] for _ in range(8)]

    
    for line in chessGame:
        if line == '':
            for column in listOfColumns:
                if ''.join(a for a in column) == '........':
                    tempMostPositions += 1
            if tempMostPositions > 0: numOfCCPositions += 1
            MostCCinPosition = MostCCPositionCheck(tempMostPositions, MostCCinPosition)
            #clearing
            tempMostPositions = 0
            for listunia in listOfColumns:
                listunia.clear()
            continue
        for i, j in enumerate(line):
            listOfColumns[i].append(j)
    
    answer = [numOfCCPositions, MostCCinPosition]
    # returning answer
    return answer

def main():
    theAnswerFinal = theLogic_column(fileAsListOfstr())
    print('%s %s' % (theAnswerFinal[0], theAnswerFinal[1]))
    return

def printing(Game):
    for i in Game:
        print(i)
    return

main()

# printing(fileAsListOfstr())
# theLogic_column(fileAsListOfstr())


