"""The Birthday Paradox, also called the Birthday Problem, is
 the surprisingly high probability that two people will have 
 the same birthday even in a small group of people. In a group 
 of 70 people, there’s a 99.9 percent chance of two people 
 having a matching birthday. But even in a group as small 
 as 23 people, there’s a 50 percent chance of a matching 
 birthday. This program performs several probability experiments 
 to determine the percentages for groups of different sizes. 
 We call these types of experiments, in which we conduct multiple 
 random trials to understand the likely outcomes, Monte Carlo experiments."""


import datetime, random


def getBirthdays(number_of_birthdays):
    #Returns a list of number random date objects for birthdays
    birthdays = []
    for i in range(number_of_birthdays):
        #The year does not matter for our simulation
        start_of_year = datetime.date(2001, 1, 1)

        #get a random day into the year:
        random_number_of_days = datetime.timedelta(random.randint(0, 364))
        birthday = start_of_year + random_number_of_days
        birthdays.append(birthday)
    return birthdays


def getMatch(birthdays):
    #Returns the date object of a birthday that occurs more than once in the b-day list:
    #for that, you will look whether the list has the same length as the list transformed
    #into a set (where there are no duplicate values)
    if len(birthdays) == len(set(birthdays)):
        return None #All bdays are unique in this case

    #compare each birthday to every other birthday:
    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a + 1: ]):
            if birthdayA == birthdayB:
                return birthdayA #return the matching birthday
    

#Display the intro now:
print('''Birthday Paradox, by Al Sweigart
The Birthday Paradox shows us that in a group of N people, the odds
that two of them have matching birthdays is surprisingly large.
This program does a Monte Carlo simulation (that is, repeated random
simulations) to explore this concept.
(It's not actually a paradox, it's just a surprising result.)''')

#Set up a tuple of month names in order:
months = ("January", "February", "March", "April", "May", "June", "July", "August", 
"September", "October", "November", "December")

while True: #keep asking until the user enters a valid amount.
    print("How many birthdays shall I generate? (max is 100):")
    response = input("> ")
    if response.isdecimal() and (0 < int(response) <= 100):
        num_bdays = int(response)
        break #User has entered a valid amount.
print()

#Generate and display the birthdays:
print(f"Here are the {num_bdays} birthdays you asked for: ")
birthdays = getBirthdays(num_bdays)
for i, birthday in enumerate(birthdays):
    if i != 0:
        #Display a comma for each birthday after the first bday:
        print(", ", end=" ")
    monthName = months[birthday.month -1]
    dateText = "{} {}".format(monthName, birthday.day)
    print(dateText, end=" ")

print()
print()


#determine whether there are two bdays matching:
match = getMatch(birthdays)

#Display the results:
print("In this simulation, ", end=" ")
if match != None:
    monthName = months[match.month -1]
    dateText = "{} {}".format(monthName, match.day)
    print(f"multiple people have their birthday on {dateText}.")
else:
    print("There are no matching bdays.")
print()

#Running through 100'000 simulations:
print(f"Generating {num_bdays} random birthdays 100'000 times...")
input("Press Enter to begin...")

print("Let's run another 100'000 simulations.")
simMatch = 0 #Find out how many simulations had matching birthdays in them:
for i in range(100000):
    #Report on the progress every 10'000 simulations:
    if i % 10000 == 0:
        print(f"{i} simulations run already...")
    birthdays = getBirthdays(num_bdays)
    if getMatch(birthdays) != None:
        simMatch += 1
print("100'000 simulations run.")

#Display simulation results:
probability = round(simMatch / 100000*100, 2)
print(f"Out of 100'000 simulations of {num_bdays} people (bdays), there was a")
print(f"matching birthday in that group {simMatch} times. This means")
print(f"that {num_bdays} people have a {probability}% chance of")
print(f"having a matching birthday in their group. That's probably more than you'd think!")


