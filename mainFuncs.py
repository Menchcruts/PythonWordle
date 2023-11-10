import os

from time import sleep
from termcolor import colored
from letterClass import Letter

COLOR_GREY = "dark_grey"
COLOR_GREEN = "green"
COLOR_YELLOW = "light_yellow"
COLOR_WHITE = "white"

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
keyboardList = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']

keyboardKeyLayout = {
    1:['q','w','e','r','t','y','u','i','o','p'],
    2:['a','s','d','f','g','h','j','k','l'],
    3:['z','x','c','v','b','n','m']
    }


def clearTerminal(sleepTime=0):
  sleep(sleepTime)
  os.system("cls")


def fileToList(filePath):
  words = []
  with open(filePath) as file:
    lines = file.readlines()
    for line in lines:
      newLine = line.replace("\n", "")
      words.append(newLine)

  return words


def evaluteGuess(guess, guessRow, secretGuess):
    
    possibleYellowIndices = []
    
    guessSplit = [*guess.lower()]
    secretSplit = [*secretGuess.lower()]


    for i in range(5):
        guessRow[i].updateLetter(guessSplit[i].upper(), COLOR_GREY)
        if guessSplit[i] == secretGuess[i]:
            guessRow[i].setColor(COLOR_GREEN)
            secretSplit[i] = ""
        else:
            possibleYellowIndices.append(i)

            
    for index in possibleYellowIndices:
        letterTemp = guessSplit[index]

        if letterTemp in secretSplit:
            guessRow[index].setColor(COLOR_YELLOW)
            secretSplit[secretSplit.index(letterTemp)] = ""
            
            
    return guessRow
    
            
def updateLettersUsed(lettersUsed, guessRow):
    letterKeys = list(lettersUsed.keys())
    for item in guessRow:
        letter = item.letter.lower()
        if letter in letterKeys and lettersUsed[letter].letterColor != COLOR_GREEN:
            lettersUsed[letter].setColor(item.letterColor)

    return lettersUsed

    
def drawBoard(board):
    boardString = ""
    title = f"     {'Wordle':^21}\n"
    subTitle = f"    {colored('Green',COLOR_GREEN)} | {colored('Yellow',COLOR_YELLOW)} | {colored('Grey',COLOR_GREY)}\n"
    
    boardString += title
    boardString += subTitle
    
    for row in board:
        rowString = "\n     "
        for item in board[row]:
            rowString += item.getArt()
        boardString += "    "
        boardString += rowString
        boardString += "\n    ---------------------\n"
        
    print(boardString)


def drawKeyboard(lettersUsed):
    lineLengths = [0,10,19,26]
    lineIndent = ["","  ","    "]
    
    finalString = ""
    for i in range(1,4):
        finalString += lineIndent[i-1]
        
        minIndex = lineLengths[i-1]
        maxIndex = lineLengths[i]

        for x in range(minIndex,maxIndex):
            tempLetter = keyboardList[x]
            if tempLetter in lettersUsed:
                tempObject = lettersUsed[tempLetter]
                tempObject.setLetter(tempLetter.upper())
            else:
                tempObject = Letter(tempLetter.upper())
            
            finalString += tempObject.getArt().replace(" ","")
        
        finalString += "\n"
    
    print(finalString)



def printRules():
    example = f" [{colored('G',COLOR_GREEN)}] [{colored('L',COLOR_YELLOW)}] [{colored('A',COLOR_GREY)}] [{colored('Z',COLOR_GREY)}] [{colored('E',COLOR_GREY)}]\n"
    title = f"{'Rules':^40}\n-----------------------------------------"    

    print(title)
    print("""Wordle is a word guessing game where you 
try and guess a five letter word in no 
more than six guesses. 
When guessing, the word you guess will 
be colored in different colors depending
on if a letter is in the secret word or 
not. 
""")
    input("Press enter to continue\n")
    clearTerminal()
    
    print(title)
    print(f"""If a letter in your guess is in the 
secret word and you've managed to put it
in the right place, the letter will be 
{colored("green",COLOR_GREEN)}. If the letter was not been in the 
right place, it would be colored {colored("yellow",COLOR_YELLOW)}.
If a letter is not in the secret word it
will be colored {colored("grey",COLOR_GREY)}.
""")
    input("Press enter to continue\n")
    clearTerminal()
    
    print(title)
    print("""Example: 
Secret word is 'Ghoul' and your guess is
'Glaze'. The following will appear when
you type it in: 
""")
    print(example)
    print("""'G' is green because it is in the word
and in the right place. 
'L' is yellow because it is in the word
but not in the right place.
All the other letters are grey because
they are not in the word. 
""")
    input("Press enter to continue\n")
    clearTerminal()
    
    print(title)
    print("""These are the rules of Wordle and I 
hope you enjoy!

Hint: If you ever want to quit in the 
middle of a game, you can write '#quit'
instead of guessing a word.          
""")
    input("Press enter to continue\n")