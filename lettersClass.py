from termcolor import colored

COLOR_GREY = "dark_grey"
COLOR_GREEN = "green"
COLOR_YELLOW = "light_yellow"
COLOR_WHITE = "white"

class Letter:
    
    def __init__(self, letter):
        self.color = COLOR_WHITE
        self.letter = letter
        self.letterArt = colored(f"[{letter}]",self.color)
        self.used = False
        
    def __str__(self):
        return self.letterArt
    
    
    def updateColor(self, newColor):
        if self.used:
            self.color = newColor
        else:
            print("Color could not be changed")
            
    def isUsed(self, boolean):
        self.used = boolean