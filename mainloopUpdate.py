# This Python file uses the following encoding: utf-8

import random

from mainFuncs import clearTerminal, drawBoard, drawKeyboard, evaluteGuess, fileToList, updateLettersUsed
from letterClass import Letter


def main(randomWord):

    #Bý til orðalistann og vel random orð
    validWords = fileToList("valid-wordle-words2.txt")
  
    if randomWord:
        secretWord = random.choice(validWords)
    else:
        secretWord = "after"
    

    #Búum til tómt leikborð
    board = {}
    for i in range(1,7):
        letterList = []
        for x in range(5):
            letterList.append(Letter())
    
        board[i] = letterList
    
    #Safn breyta fyrir stafi notaða þegar leikurinn er byrjaður
    lettersUsed = {}
    
    playing = True
    gaveUp = False
    won = False
    guessNumber = 1
    
    while playing:

        #Tæmir terminal og teiknar leikborðið og lyklaborðið
        clearTerminal()
        drawBoard(board)
        drawKeyboard(lettersUsed)
        
        if guessNumber > 6 or won:
            playing = False
            break
        
        guess = input(">> ").lower()
        guess = guess.replace(" ","")
        

        #Ef maður bara nennir ekki orðinu lengur
        if guess == "#quit":
            playing = False
            gaveUp = True
            print("You gave up")
            break
        
        won = bool(guess == secretWord)
        
        #Hér fer allt það mikilvæga fram
        if len(guess) == 5:
            if guess in validWords:

                #evaluteGuess() fer í gegnum gískið og litar stafina 
                #í þeim litum sem þeir eiga að vera 
                board[guessNumber] = evaluteGuess(guess, board[guessNumber], secretWord)
                
                #Þetta sér um að lita lyklaborðs stafina í réttum lit.
                letters = [*guess]
                for letter in letters:
                    if letter not in lettersUsed:
                        lettersUsed[letter] = Letter(letter, "white")
                lettersUsed = updateLettersUsed(lettersUsed, board[guessNumber])
                
                guessNumber += 1
           
            else:
                print("Word not found!")
                input("Please press enter to guess again\n")
        
        elif len(guess) > 5:
            print("Guess too long.")
            input("Please press enter to guess again\n")
        
        else:
            print("Guess too short.")
            input("Please press enter to guess again\n")
            

    #Outside play loop
    #Reikna stig og prenta enda skilaboð
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