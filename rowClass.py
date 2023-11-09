from termcolor import colored


COLOR_GREY = "dark_grey"
COLOR_GREEN = "green"
COLOR_YELLOW = "light_yellow"
COLOR_WHITE = "white"

class Letter:
    
    def __init__(self):
        self.letter = " "
        self.letterColor = COLOR_WHITE
    
    def updateLetter(self, newLetter, newColor):
        self.letter = newLetter
        self.letterColor = newColor
        
    def setColor(self, newColor):
        self.letterColor = newColor
        

    def getArt(self):
        return colored(f"[{self.letter}] ",self.letterColor)

