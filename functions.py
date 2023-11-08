import os

from time import sleep
from typing import ForwardRef

from termcolor import colored
from colorama import just_fix_windows_console

just_fix_windows_console()
COLOR_GREY = "dark_grey"
COLOR_GREEN = "green"
COLOR_YELLOW = "light_yellow"
COLOR_WHITE = "white"


#Initialize keybaord dictionary
used = "used"


keyboardDict = {}
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
lettersUsed = []

for letter in letters:
  keyboardDict[letter] = COLOR_WHITE


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


def drawBoard(board):
    
    print(f"{'Wordle':^21}")
    print(f"{colored('Green',COLOR_GREEN)} | {colored('Yellow',COLOR_YELLOW)} | {colored('Grey',COLOR_GREY)}\n")  

    for i in range(1, 7):
        string = " "
        list = board[i]
        for x in range(5):
            string += colored(f"[{list[x]['letter']}] ", list[x]['color'])
        print(string)
        print("---------------------\n")


def drawKeyboard():
    for x in range(2):
        string = ""
        for index in range((13*x),(13*(x+1))):
            letter = letters[index]
            string += colored(f"[{letter.upper()}]",keyboardDict[letter])
        print(string)


def drawWindow():
    
    pass

def evaluteGuess(guess, guessRow, secretWord):

  possibleYellowIndices = []

  guessSplit = [*guess]
  secretWordSplit = [*secretWord]

  for i in range(5):
    letter = guessSplit[i] 
    if letter not in lettersUsed:
       lettersUsed.append(letter)
       keyboardDict[letter] = COLOR_GREY

    guessRow[i]["color"] = COLOR_GREY
    guessRow[i]["letter"] = letter.upper()
    
  
  for i in range(5):
    if guessSplit[i] == secretWordSplit[i]:
      guessRow[i]["color"] = COLOR_GREEN
      keyboardDict[guessSplit[i]] = COLOR_GREEN
      secretWordSplit[i] = ""
      
    else:
      possibleYellowIndices.append(i)

  for index in possibleYellowIndices:
    if guessSplit[index] in secretWordSplit:
      guessRow[index]["color"] = COLOR_YELLOW
      keyboardDict[guessSplit[index]] = COLOR_YELLOW
      secretWordSplit[secretWordSplit.index(guessSplit[index])] = ""

    
  return guessRow

