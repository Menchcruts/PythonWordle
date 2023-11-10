from mainloopUpdate import main
from functions import clearTerminal
from mainFuncs import printRules

user = input("What's your name? \n")
print(f"Hello {user}!")
input("Press enter to continue.")

clearTerminal()
print("Would you like to read the rules?")
choice = input("(Y/N): ").lower()

if choice == "y":
    printRules()


playing = True
score = 0
randomWord = True

while playing:
  score += main(randomWord)
  input("Press enter to continue.")

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
  
