import time
time.sleep(0.1) # Wait for USB to become ready

print("Hello, Pi Pico!")

from ColorMatchController import *

#Be aware that there is a delay on button inputs in Wokwi so at times
#it will not pick up the button inputs during the sleep; juts keep
#pressing it and it will pick it up eventually (issue is for Wokwi)
MyGame = ColorMatchController()

MyGame.gameInitiate()