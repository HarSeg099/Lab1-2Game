import random

class ColorMatch:
    #Create a ColorMatch object with a Random generator for colors and
    #a list that will contain the colors shown and updated throughout the game
    def __init__(self):
        self._colorlist = []
    
    #fill the array with the inital color values at the start of the game
    def fillLights(self):
        sequenceVal = [WHITE, YELLOW, BLUE, RED]
        for x in range(9):
            self._colorlist.append(random.choice(sequenceVal))

    #used to add a new color to the array once a color is removed through gameplay
    def addLight(self):
        size = len(self._colorlist)
        sequenceVal = [WHITE, YELLOW, BLUE, RED]
        while size < 8:
            self._colorlist.append(random.choice(sequenceVal))
            size = len(self._colorlist)

    #remove the frontmost light color from the colorlist
    def removeLight(self):
        sequenceVal = [WHITE, YELLOW, BLUE, RED]
        self._colorlist.pop(0)
        self._colorlist.append(random.choice(sequenceVal))
            

    def compareLight(self, lightVal):
        if lightVal == 'white':
            if self._colorlist[0] == WHITE:
                return True
            else:
                return False
        elif lightVal == 'red':
            if self._colorlist[0] == RED:
                return True
            else:
                return False
        elif lightVal == 'yellow':
            if self._colorlist[0] == YELLOW:
                return True
            else:
                return False
        elif lightVal == 'blue':
            if self._colorlist[0] == BLUE:
                return True
            else:
                return False
    
    def clearColors(self):
        self._colorlist = []


#Colors taken from the LightStrip class
RED = (255, 0, 0)
YELLOW = (255, 150, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)