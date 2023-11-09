from termcolor import colored
from lettersClass import Letter
from rowClass import RowLetter

COLOR_GREY = "dark_grey"
COLOR_GREEN = "green"
COLOR_YELLOW = "light_yellow"
COLOR_WHITE = "white"


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
letterObjects = {}

for letter in letters:
    letterObjects[letter] = Letter(letter)


board = {}

for i in range(1,7):
    letterList = []
    for x in range(5):
        letterList.append(RowLetter)
    
    board[i] = letterList



def evaluteGuess(guess, guessRow, secretGuess):
    
    possibleYellowIndices = []
    
    guessSplit = [*guess]
    secretSplit = [*secretGuess]

    for item in guessSplit:
        index = guessSplit.index(item)
        guessSplit[index] = letterObjects[item]
    
    for object in guessSplit:
        object.isUsed(True)
        object.updateColor(COLOR_GREY)
        
    for i in range(5):
        if guessSplit[i].letter == secretGuess[i]:
            guessSplit[i].updateColor(COLOR_GREEN)
        else:
            possibleYellowIndices.append(i)
            
    for index in possibleYellowIndices:
        letterTemp = guessSplit[index]
        if letterTemp in secretSplit:
            guessSplit[i].updateColor(COLOR_YELLOW)
            secretSplit[secretSplit.index(letterTemp)] = ""
    
            
    

def drawBoardNew():
    boardString = ""
    title = f"{'Wordle':^21}\n"
    subTitle = f"{colored('Green',COLOR_GREEN)} | {colored('Yellow',COLOR_YELLOW)} |{colored('Grey',COLOR_GREY)}\n"
    
    boardString += title
    boardString += subTitle
    
    for row in board:
        rowString = " "
        for item in board[row]:
            rowString += item.rowLetterArt
        boardString += rowString
        boardString += "\n---------------------\n"
        
    print(boardString)