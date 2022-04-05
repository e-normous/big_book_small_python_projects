#Project 10: Cho-Han (dice game):
#Cho-han is a dice game played in
# gambling houses of feudal Japan.
# Two six-sided dice are rolled in a cup,
# and gamblers must guess if the sum is
# even (cho) or odd (han). The house takes
# a small cut of all winnings. The simple
# random number generation and basic math
# used to determine odd or even sums make
# this project especially suitable for beginners.
# More information about Cho-han can be
# found at https://en.wikipedia.org/wiki/Cho-han.


#OWN TRY START:
from random import randint
from time import sleep
import sys


def rule_explanation():
    print("Welcome to the dice game Cho-Han")
    print("We'll throw two dice that'll show values from 1 to 6")
    print("Your task is to guess whether those two values will add up to an odd or even number.")


def get_guess():
    #define the guess of the user (CHO or HAN = even or odd) and return it from the function:
    guesses = ["even", "odd", "cho", "han"]
    print("What do you think will the two dice add up to? An even (CHO) or odd (HAN) number")
    user_guess = str(input("> "))
    
    #looping through the code until the user will enter a valid input:
    while True:
        if user_guess.lower() in guesses:
            print(f"Your guess is '{user_guess.lower()}'\n")
            return user_guess.lower()
            break
        else:
            print("Sorry, you entered an invalid input.")
            print("Enter either even (CHO) or odd (HAN)")
            user_guess = str(input("> "))


def roll_the_dice():
    #define the function when the dice will roll

    #just get a random number from the random module through randint:
    dice1 = randint(1, 6)
    dice2 = randint(1, 6)
    print("The two dice have rolled. Dice one is facing...")
    sleep(2)
    print(f"Value of Dice one: {dice1}\n")
    print(f"While Dice two is facing: {dice2}\n")
    result = dice1 + dice2
    print(f"The two dice add up to {result}.\n")
    return result

def win_lose(user_guess, result):
    #decide whether the user has won or not. It is important here to check whether the result is even or odd:
    even = ["even", "cho"]
    odd = ["odd", "han"]
    if user_guess in even and result%2 == 0:
        print("You won, congrats!")
    elif user_guess in odd and result%2 == 1:
        print("You won, congrats!")
    else:
        print("Unfortunately, you lost.")

rule_explanation()

#Asking the users whether they understood the rules or they want to quit:
try:
    while True:
        print("Did you understand the rules? (yes, no or quit)")
        understood = input("> ")
        if understood.lower() == "yes":
            break
        elif understood.lower() == "quit":
            print("Thank you for using our tool")
            sys.exit()
            break
        else:
            rule_explanation()

#Catch the exception when a user interrupts the process with KeyboardInterrupt (ctrl + c)
except KeyboardInterrupt:
    print("Keyboard interrupt, the tool will close now.")


#Here this code is done without catching any exceptions. Might add this once in the future
#This is actually the point where all the functions come to their execution and where the actual game is being played:

#As long as game_on is True... well, game on:
game_on = True
while game_on == True:
    user_guess = get_guess()
    result = roll_the_dice()
    win_lose(user_guess, result)

    #asking whether the user wants to play another round:
    print("\nDo you want to play another round? (y/n)")
    play_on = str(input("> "))
    if play_on.startswith("y"):
        game_on = True
    else:
        print("Thanks for playing :-)")
        game_on = False
        sys.exit()

#OWN TRY END
