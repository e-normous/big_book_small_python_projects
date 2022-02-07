#Project 1: Bagels
#Follow the link to see the project: https://inventwithpython.com/bigbookpython/project1.html


"""In Bagels, a deductive logic game, you must guess a secret three-digit
number based on clues. The game offers one of the following hints in
response to your guess: “Pico” when your guess has a correct digit in
the wrong place, “Fermi” when your guess has a correct digit in the correct
place, and “Bagels” if your guess has no correct digits. You have 10 tries
to guess the secret number."""


import random
num_digits = 3 #The number of digits our random number will have
max_guesses = 10 #The amount of guesses the user has until he loses the game

def main():
    print(f'''Bagels, a deductive logic game.
    
I am thinking of a {num_digits}-digit number with no 
repeated digits. You'll have to guess the correct number while we'll give you some hints:

When you see:           That means:
    Pico                One digit is correct but in the wrong position
    Fermi               One digit is correct AND in the right position
    Bagel               No digit is correct

For example, if the secret number was 248 and your guess was 843, the
clues would be Fermi Pico.''' )

    while True: #This is the main game loop:
        #storing the secret number the user will have to guess:
        secretNum = getSecretNum() #getSecretNum is a function to be defined
        print("I've thought up a number.")
        print(f"You have {max_guesses} guesses to get it.")

        num_guesses = 1
        while num_guesses <= max_guesses:
            guess = ''
            #Keep looking until the user enters a valid guess:
            while len(guess) != num_digits or not guess.isdecimal():
                print(f"Guess #{num_guesses}: ")
                guess = input("> ")

            clues = getClues(guess, secretNum)
            print(clues)
            num_guesses += 1

            if guess == secretNum:
                break #if they're correct, break the loop
            if num_guesses > max_guesses:
                print("Unfortunately, you ran out of guesses.")
                print(f"The answer was {secretNum}.")

        #Ask the player if he/she wants to play again:
        again_list = ["yes", "sure", "yeah", "of course", "yay", "yap", "yup"]
        print("Do you want to play again? (yes/no): ")
        
        #That was the suggestion by Al Sweigart:
        #if not input("> ").lower().startswith("y"):
        
        #That's my suggestion:
        #again_command = str(input(""))
        if str(input("")).lower() not in again_list:
        
        
            break
    print("Thanks for playing.")

#Define the function to get the secret number:
def getSecretNum():
    numbers = list("0123456789") #create a list of digits (as strings)
    random.shuffle(numbers) #shuffle the numbers randomly
    #now get the amount of num_digits to create a random number:
    secretNum = ""
    for i in range(num_digits):
        secretNum += str(numbers[i])
    return secretNum #return the variable secretNum out of the function

def getClues(guess, secretNum):
    """Returns a string with the pico, fermi, bagels clues for a guess
    and secret number pair."""

    if guess == secretNum:
        print(f"You got it, the correct number is indeed {secretNum}. Congrats!")
    
    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]: #correct number in the correct place:
            clues.append("Fermi")
        elif guess[i] in secretNum: #correct number in the wrong place:
            clues.append("Pico")
    if len(clues) == 0:
        return "Bagels" #there are no correct guesses at all
    else:
        #sort the clues into alphabetical order so you do not giv information away:
        clues.sort()
        #now, make a string from the list of string clues:
        return " ".join(clues)

#if the program is run instead of imported, start it:
if __name__ == "__main__":
    main()