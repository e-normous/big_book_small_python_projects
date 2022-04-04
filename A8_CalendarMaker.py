#project 8: Calendar Maker https://inventwithpython.com/bigbookpython/project8.html
"""Calendar Maker, by Al Sweigart al@inventwithpython.com
Create monthly calendars, saved to a text file and fit for printing.
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: short"""

import datetime

#setting up the constants in tuples:
days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")

#Looping until you get a valid year from the user:
while True:
    print("Please enter the year you want to get the calendar from.")
    response = input("> ")

    #if the answer is a decimal number and larger than 0 (ergo a plausible year), define the year variable as an int and break the loop
    if response.isdecimal() and int(response) > 0:
        year = int(response)
        break

    #if the user does not enter a valid year, give them a hint what's a valid entry:
    print("Please enter a numberic year, like 2026")
    continue

#now get a valid month:
while True:
    print("Please enter the month for the calendar (1-12): ")
    response = input("> ")

    #In case the entry is not a decimal number, give the user a hint:
    if not response.isdecimal():
        print("Please enter a numeric month (e.g. 4 for April).")
        continue

    #if the entry is a numeric response and between (including) 1 and 12, break the loop
    month = int(response)
    if 1 <= month <= 12:
        break

    #in case that the entry is larger than 12 or less than 1, tell the user about the valid entries:
    print("Please enter a number from 1 to 12.")

print(f"Thanks for chosing the year {year} and the month {months[month -1]}.")

def getCalendarFor(year, month):
    calText = "" #This will contain the string of our calendar

    #Put the month and year at the top of the calendar:
    calText += (" " * 34) + months[month -1] + " " + str(year) + "\n"

    #Add the days of the week labels to the calendar:
    #Could also be changed to abbreviations (e.g. SUN, MON, TUE, etc.)
    calText += "...Sunday.....Monday....Tuesday...Wednesday...Thursday....Friday....Saturday..\n"

    #The horizontal line string that will separate weeks:
    weekSeparator = ("+----------" * 7) + "+\n"

    #The blank rows have ten spaces in between the | day separators:
    blankRow = ("|          " * 7) + "|\n"

    #Get the first date in the month. The datetime module handles all the complicated calendar stuff for us here:
    currentDate = datetime.date(year, month, 1)

    #Roll back currentDate until it is Sunday. weekday() returns 6 for sunday, not 0:
    while currentDate.weekday() != 6:
        currentDate -= datetime.timedelta(days=1)

    #loop over each week:
    while True: 
        calText += weekSeparator

        #dayNumberRow is the row with the day number labels:
        dayNumberRow = ""
        for i in range(7):
            dayNumberLabel = str(currentDate.day).rjust(2)
            dayNumberRow += "|" + dayNumberLabel + (" " * 8)
            currentDate += datetime.timedelta(days=1) #go to the next day
        dayNumberRow += "|\n" #add the vertical line after Saturday.


        #add the day number row and 3 blank rows to the calendar text:
        calText += dayNumberRow
        for i in range(3): #what will happen if you change the 4 to a 5 or 10?
            calText += blankRow

        #Check if we're done with the month:
        if currentDate.month != month:
            break

    #add the horizontal line at the very bottom of the calendar:
    calText += weekSeparator
    return calText

calText = getCalendarFor(year, month)
#Display the calendar:
print(calText) 

#Save the calendar to a text file:
calendarFilename = f"calendar_{year}_{month}.txt"
with open(calendarFilename, "w") as fileObj:
    fileObj.write(calText)

print(f"Saved to {calendarFilename}")


