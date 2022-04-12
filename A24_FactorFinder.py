#project 24: Factor Finder
"""A number’s factors are any two other numbers that, when multiplied with each other,
produce the number. For example, 2 × 13 = 26, so 2 and 13 are factors of 26. Also, 1 × 26 = 26,
so 1 and 26 are also factors of 26. Therefore, we say that 26 has four factors: 1, 2, 13, and 26.

If a number only has two factors (1 and itself), we call that a prime number. Otherwise, we
call it a composite number. Use the factor finder to discover some new prime numbers!
(Hint: Prime numbers always end with an odd number that isn’t 5.) You can also have the
computer calculate them with Project 56, “Prime Numbers.”

The math for this program isn’t too heavy, making it an ideal project for beginners."""


#importing the needed modules:
import math, sys


print('''Factor Finder, by Al Sweigart al@inventwithpython.com

A number's factors are two numbers that, when multiplied with each
other, produce the number. For example, 2 x 13 = 26, so 2 and 13 are
factors of 26. 1 x 26 = 26, so 1 and 26 are also factors of 26. We
say that 26 has four factors: 1, 2, 13, and 26.
 
If a number only has two factors (1 and itself), we call that a prime
number. Otherwise, we call it a composite number.
 
Can you discover some prime numbers?''')

#addition by MWE to find out whether we have a prime number:
def prime_number(factors):
    if len(factors) <= 2:
        print(f"We have a prime number here:")
        if len(factors) == 1:
            print(factors[0])
        else:
            print(factors[1])


#main program loop:
while True:
    print("Enter a positive whole number to factor (or enter QUIT):")
    response = input("> ")
    if response.upper()== "QUIT":
        print("Exiting...")
        sys.exit()
    
    #if the response fits the needed elements, make the int a new variable (number) and an integer:
    if not (response.isdecimal() and int(response) > 0):
        continue
    number = int(response)

    #we'll save the factors in a list for later use:
    factors = []

    #find the factors of number:
    for i in range(1, int(math.sqrt(number)) +1):

        #if there's no remainder, it is a factor
        if number % i == 0:
            factors.append(i)
            factors.append(number // i)

    #convert to a set to get rid of duplicate factors:
    factors = list(set(factors))
    factors.sort()

    #display the results:
    print("Factors are: ")
    for i, factor in enumerate(factors):
        factors[i] = str(factor)
    print(', '.join(factors))

    #getting the prime numbers:
    prime_number(factors)

