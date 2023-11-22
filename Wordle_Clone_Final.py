# This Python file uses the following encoding: utf-8

from mainloopUpdate import main
from mainFuncs import printRules, clearTerminal, checkDate, randomWord

from colorama import just_fix_windows_console

#�etta l�tur terminal-i� geta skrifa� texta � lit
just_fix_windows_console()

wordOfDayFinished = True
newDay = checkDate()

newDay = False

user = input("What's your name? \n")
print(f"Hello {user}!")
input("Press enter to continue.")

#clearTeminal() er fall sem gerir n�kv�mlega �a� sem �a� heitir, 
#e�a strokar �t allan texta � terminal-inu.
clearTerminal()

if newDay:
    wordOfDayFinished = False
    print("Would you like to play the Wordle of the day?")
    choiceWord = input("(Y/N): ").lower()
    if choiceWord == "y":
        doingWordOfDay = True
    else:
        doingWordOfDay = False


print("Would you like to read the rules?")
choice = input("(Y/N): ").lower()

if choice == "y":
    printRules()


playing = True
totalScore = 0

randomWord = False

while playing:
    score = main(randomWord)
    input("Press enter to continue.")

    #while l�ppa � me�an leikma�ur er a� �kve�a sig. 
    while True:
        clearTerminal()
    
        totalScore += score
        print(f"You got {score} points this round.")
        print(f"You now have a total of {totalScore} points.")


        print("Do you want to play again?")
    
        choice = input("(Y/N): ")
        choice = choice.replace(" ","")
  
        if choice.lower() == "y":
            print("Then lets start!")
            clearTerminal(1)
            break
        elif choice.lower() == "n":
            print("Ok, bye!")
            clearTerminal(0.75)
            playing = False
            break
        else:
            print("Invalid choice. Please try again.")
            clearTerminal(1)
  
