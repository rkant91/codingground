'''Write a Python script to display the - a) Current date and time b) Current year c) Month of year d) Week number of the year
                e) Weekday of the week f) Day of year g) Day of the month h) Day of week */'''
import time, calendar

def printDates():
    print "Time in ticks: ",time.time(); #returns the current system time in ticks since 12:00am, January 1, 1970(epoch)
    localtime = time.asctime(time.localtime(time.time()));
    print "Current local time : ",localtime
    print "Calendar for Nov, 2016 is below: \n",calendar.month(2016,11);
    
    
    return
    
    
    
    
    
    return
                                          
                                          
