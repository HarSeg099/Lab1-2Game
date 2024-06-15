import time
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
        self._gameState = False
        self._gameStart = False
        self._highScore = 50
        
    #This will work with the game method to pop the colors from the ColorMatch's object
    #internal list as they're pressed    
    def buttonPressed(self, name):
        if self._gameState == True:
            if name == 'white':
                if self._colormatch.compareLight(name) == True:
                     self._score = self._score + 1
                     self.replaceLight()
                     self._buzzer.beep(1000)
                     self.buttonPressed(name)
                else:
                    pass
            elif name == 'red':
                if self._colormatch.compareLight(name) == True:
                     self._score = self._score + 1
                     self.replaceLight()
                     self._buzzer.beep(1000)
                     self.buttonPressed(name)
                else:
                    pass
            elif name == 'yellow':
                if self._colormatch.compareLight(name) == True:
                     self._score = self._score + 1
                     self.replaceLight()
                     self._buzzer.beep(1000)
                     self.buttonPressed(name)
                else:
                    pass
            elif name == 'blue':
                if self._colormatch.compareLight(name) == True:
                     self._score = self._score + 1
                     self.replaceLight()
                     self._buzzer.beep(1000)
                     self.buttonPressed(name)
                else:
                    pass
        elif self._gameStart == False:
            if name == 'black':
                self._gameStart == True
                self.game()
        else:
            pass
    
    #Starts the game upon player input
    def gameInitiate(self):
        self._display.reset()
        self._display.showText(f'Press Black')
        self._display.showText(f'To Start',row=1)

    #Main game method
    def game(self):
        self._colormatch.fillLights() #Get a random array of colors

        #Turns on the individual lights the different array of colors
        for x in range(0, len(self._colormatch._colorlist)-1):
            self._lightstrip.setPixel(pixelno = x, color = self._colormatch._colorlist[x])
        self._counter.start()

        #Whill show the time ticking up for a minute while the game runs
        self._display.reset() #Clear the screen before the game
        self._gameState = True
        #Be aware that there is a delay on button inputs in Wokwi so at times
        #it will not pick up the button inputs during the sleep; juts keep
        #pressing it and it will pick it up eventually (issue is for Wokwi)
        while self._counter.getMin() < 1:
            self._display.showText(f'Timer: {self._counter.getSec()}')
            self._display.showText(f'Score: {self.getScore()}',row=1)

            if self._buttons[0].isPressed() == True:
                self.buttonPressed(self._buttons[0].getName())
            if self._buttons[1].isPressed() == True:
                self.buttonPressed(self._buttons[1].getName())
            if self._buttons[2].isPressed() == True:
                self.buttonPressed(self._buttons[2].getName())
            if self._buttons[3].isPressed() == True:
                self.buttonPressed(self._buttons[3].getName())

            time.sleep(0.333)
        self._counter.stop()
        
        if(self._score > self._highScore):
            self._display.reset()
            self._display.showText('New HighScore!')
            self._display.showText(f'Your Score: {self.getScore()}', row = 1)
            self._highScore = self._score
            self._buzzer.beep(1000)
            time.sleep(5)
        else:
            self._display.reset()
            self._display.showText(f'HighScore: {self.getHighScore()}')
            self._display.showText(f'Your Score: {self.getScore()}', row = 1)
            self._buzzer.beep()
            time.sleep(5)

        self._display.reset()
        self._display.showText('Resetting to')
        self._display.showText('start a new game', row = 1)
        self.resetGame()

    #replace the light at the back with the newest color
    #while removing the one pressed
    def replaceLight(self):
        self._colormatch.removeLight()
        for x in range(0, len(self._colormatch._colorlist)-1):
            self._lightstrip.setPixel(pixelno = x, color = self._colormatch._colorlist[x])

    #return the value of the _score attribute
    def getScore(self):
        tempScore = self._score
        return tempScore

    #return the value of the _highScore attribute
    def getHighScore(self):
        tempScore = self._highScore
        return tempScore

    #this will reset the game so it begins again.
    def resetGame(self):
        self._score = 0
        self._colormatch.clearColors()
        self._counter.reset()
        self._gameState = False
        self._gameStart = False
        self._lightstrip.off()
        self.gameInitiate()

    #Just here so it stops throwing an error that I don't have it...
    def buttonReleased(self, name):
        pass