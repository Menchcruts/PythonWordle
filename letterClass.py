from termcolor import colored


COLOR_GREY = "dark_grey"
COLOR_GREEN = "green"
COLOR_YELLOW = "light_yellow"
COLOR_WHITE = "white"

class Letter:
    
    def __init__(self, letter=" ", color = COLOR_WHITE):
        self.letter = letter
        self.letterColor = color
        
    def __str__(self):
        return f"{self.letter}, {self.letterColor}"
    
    def updateLetter(self, newLetter, newColor):
        self.letter = newLetter
        self.letterColor = newColor
        
    def setColor(self, newColor):
        self.letterColor = newColor
        
    def setLetter(self, newLetter):
        self.letter = newLetter
        
    #Sendir litaðann stafinn í 'kassa', eða [], til baka
    def getArt(self):
        return colored(f"[{self.letter}] ",self.letterColor)

