from Displays import LCDDisplay
from Button import *
from Clock import *


class ClockController:
    """ Our implementation of the Clock Controller
        4 buttons for setting month, date, hour, min
        LCD display to show the time
    """

    def __init__(self):
        self._clock = Clock()
        self._display = LCDDisplay(sda=0, scl=1, i2cid=0)
        self._buttons = [Button(10, 'white', buttonhandler=self),
                        Button(11, 'red', buttonhandler=self),
                        Button(12, 'yellow', buttonhandler=self),
                        Button(13, 'blue', buttonhandler=self)]
    
    def showTime(self):
        #Show the time on the display
        
        (year, month, date, hour, minute, sec, wd, yd) = self._clock.getTime()

        if (month in {1,2,12}):
            self._display.showText(f'{month}/{date}/{year} Win ')
            self._display.showText(f'{hour:0>2}:{minute:0>2}:{sec:0>2} Cold  ', row=1)
        elif (month in {3,4,5}):
            self._display.showText(f'{month}/{date}/{year} Spr ')
            self._display.showText(f'{hour:0>2}:{minute:0>2}:{sec:0>2} Rainy', row=1)
        elif (month in {6,7,8}):
            self._display.showText(f'{month}/{date}/{year} Sum ')
            self._display.showText(f'{hour:0>2}:{minute:0>2}:{sec:0>2} Hot  ', row=1)
        else:
            self._display.showText(f'{month}/{date}/{year} Fall')
            self._display.showText(f'{hour:0>2}:{minute:0>2}:{sec:0>2} Chilly', row=1)

    def buttonPressed(self, name):
        if name == 'yellow':
            # get the current hour
            hour = self._clock.getHour()

            # set the hour to 1 + the current hour
            # if this causes the hour to go over 23, sets hour to 0 and calls func
            # to increase day
            if (hour + 1) < 24:
                self._clock.setHour(hour + 1)
            else:
                self._clock.setHour(0)
                self.buttonPressed('red')        
        elif name == 'blue' :
            # get the current minute
            minute = self._clock.getMinute()
            
            #set the minute to 1 + the current minute or set minute to 0 and call the
            #function recursively with the argument to increase hour if 1 + minute is
            #greater than or equal to 60
            if (minute + 1) < 60:
                self._clock.setMinute(minute + 1)
            else:
                self._clock.setMinute(0)
                self.buttonPressed('yellow')
        elif name == 'red' :
            # get the current date
            date = self._clock.getDate()
            # get the current month
            month = self._clock.getMonth()
            
            #set the minute to 1 + the current date or set date to 1 and call the
            #function recursively with the argument to increase month if 1 + month
            #is greater than or equal to the max number of days in the month
            if (month in {1,3,5,7,8,10,12}):
                if (date + 1) < 32:
                    self._clock.setDate(date + 1)
                else:
                    self._clock.setDate(1)
                    self.buttonPressed('white')
            elif (month in {4,6,9,11}):
                if (date + 1) < 31:
                    self._clock.setDate(date + 1)
                else: 
                    self._clock.setDate(1)
                    self.buttonPressed('white')
            else:
                if self._clock.getYear() % 4 == 0:
                    if (date + 1) < 30:
                        self._clock.setDate(date + 1)
                    else:
                        self._clock.setDate(1)
                        self.buttonPressed('white')
                else:
                    if (date + 1) < 29:
                        self._clock.setDate(date + 1)
                    else:
                        self._clock.setDate(1)
                        self.buttonPressed('white')
        elif name == 'white' :
            # get the current month
            month = self._clock.getMonth()
            # get the current year
            year = self._clock.getYear()
            
            #set the month to 1 + the current month or if over 12, move to new year
            #and set month to January
            if (month + 1) < 13:
                self._clock.setMonth(month + 1)
            else:
                self._clock.setMionth(1)
                self._clock.setYear(self._clock.getYear() + 1)

    def buttonReleased(self,name):
        pass
