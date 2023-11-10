import random

from mainFuncs import clearTerminal, drawBoard, drawKeyboard, evaluteGuess, fileToList, updateLettersUsed
from letterClass import Letter


def main(randomWord):

    #B� til or�alistann og vel random or�
    validWords = fileToList("valid-wordle-words2.txt")
  
    if randomWord:
        secretWord = random.choice(validWords)
    else:
        secretWord = "ghoul"
    

    #B�um til t�mt leikbor�
    board = {}
    for i in range(1,7):
        letterList = []
        for x in range(5):
            letterList.append(Letter())
    
        board[i] = letterList
    
    #Safn breyta fyrir stafi nota�a �egar leikurinn er byrja�ur
    lettersUsed = {}


    playing = True
    gaveUp = False
    won = False
    guessNumber = 1
    
    while playing:
        
        #T�mir terminal og teiknar leikbor�i� og �� 'lyklabor�i�'
        clearTerminal()
        drawBoard(board)
        drawKeyboard(lettersUsed)
        
        if guessNumber > 6 or won:
            playing = False
            break
        
        guess = input(">> ").lower()
        guess = guess.replace(" ","")
        

        #Ef ma�ur bara nennir ekki or�inu lengur
        if guess == "#quit":
            playing = False
            gaveUp = True
            print("You gave up")
            break
        
        won = bool(guess == secretWord)
        
        #H�r fer allt �a� mikilv�ga fram
        if guess in validWords:
            if len(guess) == 5:
                
                #evaluteGuess() fer � gegnum g�ski� og litar stafina 
                #� �eim litum sem �eir eiga a� vera 
                board[guessNumber] = evaluteGuess(guess, board[guessNumber], secretWord)
                
                #�etta s�r um a� lita lyklabor�s stafina � r�ttum lit.
                letters = [*guess]
                for letter in letters:
                    if letter not in lettersUsed:
                        lettersUsed[letter] = Letter(letter, "white")
                lettersUsed = updateLettersUsed(lettersUsed, board[guessNumber])
                
                guessNumber += 1

        
            elif len(guess) > 5:
                print("Guess too long.")
                input("Please press enter to guess again\n")
        
            else:
                print("Guess too short.")
                input("Please press enter to guess again\n")
        else:
            print("Word not found!")
            input("Please press enter to guess again\n")
            

        

    #Outside play loop
    #Reikna stig og prenta enda skilabo�
    score = (6-(guessNumber - 2)) if won else 0
    if won:
        print(f"You guessed the word in {guessNumber-1} guesses so you get {score} points.")
        print(f"The word was {secretWord.title()}")
        return score 
    else:
        if not gaveUp:
            print("You ran out of guesses. Bummer.")
        print(f"The word was {secretWord.title()}")
        return score