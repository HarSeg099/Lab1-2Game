import time
time.sleep(0.1) # Wait for USB to become ready

print("Hello, Pi Pico!")

from ColorMatchController import *

#instantiates the ColorMatchController
myColorMatch = ColorMatchController()

while True:
    #Waits for button input to continue
    #if GPIO.input(button):
    #    myColorMatch.buttonReleased()

    if myColorMatch.buttonReleased(black) == True:
        myColorMatch.buttonReleased(black)




