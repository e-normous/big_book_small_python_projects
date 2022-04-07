#Project 12 - COLLATZ SEQUENCE:

"""The Collatz sequence, also called the 3n + 1 problem,
is the simplest impossible math problem. (But don’t worry,
the program itself is easy enough for beginners.) From a
starting number, n, follow three rules to get the next number in
the sequence:

If n is even, the next number n is n / 2.
If n is odd, the next number n is n * 3 + 1.
If n is 1, stop. Otherwise, repeat.
It is generally thought, but so far not 
mathematically proven, that every starting number
eventually terminates at 1. More information about the Collatz
sequence can be found at https://en.wikipedia.org/wiki/Collatz_conjecture."""


#MWE self try:

import sys
from time import sleep


def number_is_one(n):
    print("'n' is 1, therefore we're going to break our loop and finish the program.")
    

#defining what to do when you have an even or odd number. Print orders are "commented"
#(could be used to check the code):
def even_number(n):
    #print(f"Your number 'n' (={n}) is an even number.")
    n = int(n/2)
    #print(f"Therefore, we divide 'n' through two, resulting in {n}.")
    #sleep(0.1)
    return n

def odd_number(n):
    #print(f"Your number 'n' (={n}) is an odd number. ")
    n = int((n*3)+1)
    #print(f"Therefore, we'll calculate n = n*3+1, resulting in {n}")
    #sleep(0.1)
    return n


#the actual program:
#get the user input and loop until they enter a valid entry:
n = "no number"

try:
    while n.isdecimal() != True or n == "0":
        print("Please enter a number other than zero for which we'll calculate the Collatz sequence: ")
        n = input("> ")

#catch the exception when a user interrupts the program:
except KeyboardInterrupt:
    print("You've interrupted the program and may finish it now.")
    sys.exit()

#now after we've checked that the user input is a decimal, make it indeed an int:
n = int(n)

#also save the user input in a separate variable to re-use it at the end:
sequence = n

#Tell the user what they've just entered:
print(f"You have chosen 'n' to be the number {n}")

#loop through n for as long as it is not one (make a difference for odd and even numbers)
#define an empty list (or add the starting point) to print out all the numbers in the sequence at the end:
n_list = [sequence]
while n != 1:

    #if n is an even number, use the even function:
    if n % 2 == 0:
        n = even_number(n)
        n_list.append(n)

    #if n is an odd number, use the odd function:
    elif n % 2 == 1:
       n = odd_number(n)
       n_list.append(n)

#when n is 1, use the number_is_one function (actually not needed when we don't print anything
# up to now)
#number_is_one(n)


print(f"The following numbers are part of the sequence you've asked for (n = {sequence}):\n{n_list}")
print(f"That's {len(n_list)} numbers!")


sys.exit()