###program which lets the user know if it is a weekday or the weekend
###shouldnt require any user input of the date


import datetime  ##this will allow python to access the current date
import calendar     ###allows us to compare dates to days
x = datetime.date.today()  ##pulls the date the program is being run on

weekend_check = calendar.weekday(x.year,x.month,x.day)      
##the above changes the date to a day of the week
##the date stored in x must be split into year, month and day for the weekday function to work
if weekend_check < 5:
    ##weekdays are stored as numbers, with monday = 0. so anything less than 5 is a weekday
    print ("Today is a weekday, unlucky :(")
else:
    ###only 2 options, so else is sufficient, no need for elif.
    print("Hurray! It's the weekend!")