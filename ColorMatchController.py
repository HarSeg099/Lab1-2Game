from Displays import LCDDisplay
from Button import *
from Buzzer import PassiveBuzzer
from Counters import TimeKeeper
from ColorMatch import *
from Lights import *
from LightStrip import *

class ColorMatchController:

    #Instantiates ColorMatchController class that contains most of the hardware,
    #a Timer, and a ColorMatch object
    def __init__(self):
        self._score = 0
        self._colormatch = ColorMatch()
        self._counter = TimeKeeper()
        self._display = LCDDisplay(sda=0, scl=1, i2cid=0)
        self._buttons = [Button(10, 'white', buttonhandler=self),
                        Button(11, 'red', buttonhandler=self),
                        Button(12, 'yellow', buttonhandler=self),
                        Button(13, 'blue', buttonhandler=self),
                        Button(14, 'black', buttonhandler=self)]
        self._buzzer = PassiveBuzzer(16)
        self._lightstrip = LightStrip(name="My light strip", pin=2, numleds=8)
        
    #This will work with the game method to pop the colors from the ColorMatch's object
    #internal list as they're pressed    
    def buttonPressed(self, name):
        if name == 'white':
            #this will removed it for white and the other colors will be implemented
            #and remove it for them accordingly
            pass
        else:
            pass

    #Ended up using button release as a way to start the game
    def buttonReleased(self, name):
        if name == 'black':
            self._display.reset()
            self.game()
        else:
            self._display.showText(f'Press White')
            self._display.showText(f'To Start',row=1)
    
    #Main game method
    def game(self):
        self._colormatch.fillLights() #Get a random array of colors

        lightlist = self._colormatch._colorlist 

        #Turns on the individual lights the different array of colors
        for x in range(0, len(lightlist)-1):
            self._lightstrip.setPixel(pixelno = x, color = lightlist[x])
        self._counter.start()

        #Whill show the time ticking up for a minute while the game runs
        while True:
            self._display.showNumber(f'Timer: {self._counter.getSec()}')
            self._display.showNumber(f'Score: {self.getScore()}',row=1)

            ''' From here foward will the game continue to run as the time ticks
            up toa minute'''

    def replaceLight(self):
        '''This method will be called within game to replace the light'''

    #returna the value of the _score attribute
    def getScore(self):
        tempScore = self._score
        return tempScore

    #this will reset the game so it begins again.
    def resetGame(self):
        pass

    #this will be the starting game method
    def initializeGame(self):
        pass
        

