
import random

from functions import clearTerminal, drawBoard, drawKeyboard, evaluteGuess, fileToList


def main(randomWord):

  validWords = fileToList("valid-wordle-words.txt")
  
  if randomWord:
    secretWord = random.choice(validWords)
  else:
    secretWord = "chode"
  
  
  
  LETTER = "letter"
  COLOR = "color"
  COLOR_WHITE = "white"
  
  board = {
      1: [{
          LETTER: " ",
          COLOR: COLOR_WHITE
      }, {
          LETTER: " ",
          COLOR: COLOR_WHITE
      }, {
          LETTER: " ",
          COLOR: COLOR_WHITE
      }, {
          LETTER: " ",
          COLOR: COLOR_WHITE
      }, {
          LETTER: " ",
          COLOR: COLOR_WHITE
      }],
      2: [{
          LETTER: " ",
          COLOR: COLOR_WHITE
      }, {
          LETTER: " ",
          COLOR: COLOR_WHITE
      }, {
          LETTER: " ",
          COLOR: COLOR_WHITE
      }, {
          LETTER: " ",
          COLOR: COLOR_WHITE
      }, {
          LETTER: " ",
          COLOR: COLOR_WHITE
      }],
      3: [{
          LETTER: " ",
          COLOR: COLOR_WHITE
      }, {
          LETTER: " ",
          COLOR: COLOR_WHITE
      }, {
          LETTER: " ",
          COLOR: COLOR_WHITE
      }, {
          LETTER: " ",
          COLOR: COLOR_WHITE
      }, {
          LETTER: " ",
          COLOR: COLOR_WHITE
      }],
      4: [{
          LETTER: " ",
          COLOR: COLOR_WHITE
      }, {
          LETTER: " ",
          COLOR: COLOR_WHITE
      }, {
          LETTER: " ",
          COLOR: COLOR_WHITE
      }, {
          LETTER: " ",
          COLOR: COLOR_WHITE
      }, {
          LETTER: " ",
          COLOR: COLOR_WHITE
      }],
      5: [{
          LETTER: " ",
          COLOR: COLOR_WHITE
      }, {
          LETTER: " ",
          COLOR: COLOR_WHITE
      }, {
          LETTER: " ",
          COLOR: COLOR_WHITE
      }, {
          LETTER: " ",
          COLOR: COLOR_WHITE
      }, {
          LETTER: " ",
          COLOR: COLOR_WHITE
      }],
      6: [{
          LETTER: " ",
          COLOR: COLOR_WHITE
      }, {
          LETTER: " ",
          COLOR: COLOR_WHITE
      }, {
          LETTER: " ",
          COLOR: COLOR_WHITE
      }, {
          LETTER: " ",
          COLOR: COLOR_WHITE
      }, {
          LETTER: " ",
          COLOR: COLOR_WHITE
      }],
  }
  
  playing = True
  won = False
  guessNumber = 1
  guesses = []
  
  while playing:
    clearTerminal()
    drawBoard(board)
    drawKeyboard()
  
    if guessNumber > 6 or won:
      playing = False
      break
  
    guess = input().lower()
    guess = guess.replace(" ", "")
  
    won = bool(guess == secretWord)
  
    if len(guess) == 5:
    
      guessValid = bool(guess in validWords)
      alreadyGuessed = bool(guess in guesses)
  
      if guessValid and not alreadyGuessed:
        board[guessNumber] = evaluteGuess(guess, board[guessNumber], secretWord)
  
        guesses.append(guess)
        guessNumber += 1
  
  
      elif alreadyGuessed:
        print(f"You've already guessed {guess.title()}")
        input("\nPress enter to guess again.")
  
      else:
        print(f"{guess.title()} is not a valid word.")
        input("\nPress enter to guess again.")
  
    elif len(guess) > 5:
      print("Guess too long")
      input("\nPress enter to guess again.")
      
    else:
      print("Guess too short")
      input("\nPress enter to guess again.")
  
  if won:
    print(f"You got the word in {guessNumber-1} guesses. Congratulations!")
    print(f"The word was {secretWord.title()}")
    return 1
  
  else:
    print("You ran out of guesses. Bummer.")
    print(f"The word was {secretWord.title()}")
    return 0
  