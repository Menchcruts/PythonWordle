# This Python file uses the following encoding: utf-8

from mainloopUpdate import main
from mainFuncs import printRules, clearTerminal, checkDate

from colorama import just_fix_windows_console

#�etta l�tur terminal-i� geta skrifa� texta � lit
just_fix_windows_console()

newDay = checkDate()
print(newDay)

user = input("What's your name? \n")
print(f"Hello {user}!")
input("Press enter to continue.")

#clearTeminal() er fall sem gerir n�kv�mlega �a� sem �a� heitir, 
#e�a strokar �t allan texta � terminal-inu.
clearTerminal()

print("Would you like to read the rules?")
choice = input("(Y/N): ").lower()

if choice == "y":
    printRules()


playing = True
score = 0
randomWord = False

while playing:
  score += main(randomWord)
  input("Press enter to continue.")

  #while l�ppa � me�an leikma�ur er a� �kve�a sig. 
  while True:
    clearTerminal()
    
    print(f"You have {score} points.")
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
  
