from Counters import Time
from machine import RTC

class Clock:
    """
    Our implementation of the Clock class
    """

    def getTime(self):
        #return the current time
        return Time.getTime()

    def setTime(self, timetuple):
        Time.setTime(timetuple)

    def getHour(self):
        # return the current hour as an int

        timetuple = Time.getTime()
        return timetuple[3]
    
    def setHour(self, hour):
        #Sets the RTC Hour to the hour parameter
        #First get the current time from the system
        timetuple = Time.getTime()
        #Convert the tuple into a list
        timelist = list(timetuple)
        #Change the hour to the new hour
        timelist[3] = hour
        #Save it back to the system
        Time.setTime(timelist)

    def getMinute(self):
        timetuple = Time.getTime()
        return timetuple[4]

    def setMinute(self, minute):
        timetuple = Time.getTime()
        timelist = list(timetuple)
        timelist[4] = minute
        Time.setTime(timelist)

    def getDate(self):
        timetuple = Time.getTime()
        return timetuple[2]
    
    def setDate(self, date):
        timetuple = Time.getTime()
        timelist = list(timetuple)
        timelist[2] = date
        Time.setTime(timelist)

    def getMonth(self):
        timetuple = Time.getTime()
        return timetuple[1]

    def setMonth(self, month):
        timetuple = Time.getTime()
        timelist = list(timetuple)
        timelist[1] = month
        Time.setTime(timelist)
    
    def getYear(self):
        timetuple = Time.getTime()
        return timetuple[0]

    def setYear(self, year):
        timetuple = Time.getTime()
        timelist = list(timetuple)
        timelist[0] = year
        Time.setTime(timelist)
