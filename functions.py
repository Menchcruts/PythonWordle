import os

from time import sleep

from termcolor import colored
from colorama import just_fix_windows_console

just_fix_windows_console()
COLOR_GREY = "dark_grey"
COLOR_GREEN = "green"
COLOR_YELLOW = "light_yellow"
COLOR_WHITE = "white"


#Initialize keybaord dictionary
keyboardDict = {}
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
keyboardList = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
lettersUsed = []
keyboardLayout = f"""
[{0}][{1}][{2}][{3}][{4}][{5}][{6}][{7}][{8}][{9}]
  [{10}][{11}][{12}][{13}][{14}][{15}][{16}][{17}][{18}]
    [{19}][{20}][{21}][{22}][{23}][{24}][{25}]"""


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
    finalString = ""
    finalString += f"{'Wordle':^21}\n"
    finalString += f"{colored('Green',COLOR_GREEN)} | {colored('Yellow',COLOR_YELLOW)} | {colored('Grey',COLOR_GREY)}\n\n"

    for i in range(1, 7):
        string = " "
        list = board[i]
        for x in range(5):
            string += colored(f"[{list[x]['letter']}] ", list[x]['color'])
        string += "\n---------------------\n"
        finalString += string
    print(finalString)


def drawKeyboard():
    finalString = ""
    for x in range(2):
        string = ""
        for index in range((13*x),(13*(x+1))):
            letter = letters[index]
            string += colored(f"[{letter.upper()}]",keyboardDict[letter])
        finalString += string
        finalString += "\n"
    print(finalString)

def drawKeyboard2():
   finalString = f""
   
   string = f""
   for x in range(10):
       letter = keyboardList[x]
       string += colored(f"[{letter.upper()}]",keyboardDict[letter])
   finalString += f"{string:^30}"
   finalString += "\n"
   
   string = f""
   for x in range(10,19):
        letter = keyboardList[x]
        string += colored(f"[{letter.upper()}]",keyboardDict[letter])
   finalString += f"{string:^30}"
   finalString += "\n"
   
   string = f""
   for x in range(20,26):
        letter = keyboardList[x]
        string += colored(f"[{letter.upper()}]",keyboardDict[letter])
   finalString += f"{string:^30}"
   finalString += "\n"
   
   print(finalString)


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

