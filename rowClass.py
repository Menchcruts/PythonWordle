from termcolor import colored


COLOR_GREY = "dark_grey"
COLOR_GREEN = "green"
COLOR_YELLOW = "light_yellow"
COLOR_WHITE = "white"

class RowLetter:
    
    def __init__(self):
        self.rowLetter = ""
        self.letterColor = COLOR_WHITE
        self.rowLetterArt = colored(f"[{self.rowLetter}]",self.letterColor)
        
    def __str__(self):
        return self.rowLetterArt
    
    def updateLetter(self,newLetter, newColor):
        self.rowLetter = newLetter
        self.letterColor = newColor
        

