#project 26: Fibonacci

"""The Fibonacci sequence is a famous mathematical
pattern credited to Italian mathematician Fibonacci
in the 13th century (though others had discovered it
even earlier). The sequence begins with 0 and 1, and
the next number is always the sum of the previous
two numbers. The sequence continues forever:

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987 . . .

The Fibonacci sequence has applications in music
composition, stock market prediction, the pattern
of florets in the head of sunflowers, and many other areas.
This program lets you calculate the sequence as high as
you are willing to go. More information about the
Fibonacci sequence can be found
at https://en.wikipedia.org/wiki/Fibonacci_number."""



#importing the needed module:
import sys

#main loop:
while True:
    #Keep asking until there's a valid user input:
    while True:
        print("Enter the 'nth' Fibonacci number you wish to")
        print("calculate (such as 5, 50, 700, 9999) or QUIT to quit: ")
        response = input("> ").upper()

        if response == "QUIT":
            print("Thanks for using the tool.")
            sys.exit()
        
        if response.isdecimal() and int(response) != 0:
            nth = int(response)
            break

        print("Please enter a number greater than 0 or QUIT.")
    print()

    #If user input is 1 or 2, these are special cases:
    if nth == 1:
        print("0")
        print()
        print("The #1 Fibonacci number is 0.")
        continue

    elif nth == 2:
        print("0, 1")
        print()
        print("The #2 Fibonacci number is 1.")

    #display a warning if the user input is rather high:
    if nth >= 10000:
        print(f"WARNING: You've entered {nth}. This will take quite some time")
        print("to display on the screen. If you want")
        print("to quit the program early, press CTRL+C")
        input("Press enter to begin...")

    #calculating the nth Fibonacci number:
    second_to_last_number = 0
    last_number = 1
    fib_numbers_calculated = 2

    #display the very first fibonacci numbers (special case):
    print("0, 1, ", end="")

    #display all later numbers of the sequence:
    while True:
        next_number = second_to_last_number + last_number
        fib_numbers_calculated += 1

        #display the next number in the sequence:
        print(next_number, end="")

        #check if we've found the nth number the user wants:
        if fib_numbers_calculated == nth:
            print()
            print()
            print(f"The #{fib_numbers_calculated} Fibonacci number is {next_number}.")
            break

        #print a comma in between the sequence numbers:
        print(", ", end = "")

        #shift the last two numbers:
        second_to_last_number = last_number
        last_number = next_number