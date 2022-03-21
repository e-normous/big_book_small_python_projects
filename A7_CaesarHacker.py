#project 7: Caesar hacker https://inventwithpython.com/bigbookpython/project7.html

"""Caesar Cipher Hacker, by Al Sweigart al@inventwithpython.com
 This programs hacks messages encrypted with the Caesar cipher by doing
 a brute force attack against every possible key.
 More info at:
 https://en.wikipedia.org/wiki/Caesar_cipher#Breaking_the_cipher
 This code is available at https://nostarch.com/big-book-small-python-programming
 Tags: tiny, beginner, cryptography, math"""


print("Please enter the encrypted Caesar cipher message to hack.")
message = input("> ").upper()

#Every possible symbol that can be encrypted/decrypted:
#This must match the symbols used when encrypting the message:
symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

#looping through every possible key:
for key in range(len(symbols)):
    translated = ""

    #Decrypt each symbol in the message:
    for symbol in message:
        if symbol in symbols:
            #Get the number of the symbol:
            num = symbols.find(symbol)
            #Decrypt the number:
            num -= key

            #Handle the wrap-around if num is less than 0:
            if num < 0:
                num += len(symbols)

            #Add the decrypted number's symbol to translated:
            translated += symbols[num]
        else:
            #just add the symbol without decrypting:
            translated += symbol
    
    #Display the key being tested, along with its decrypted text:
    print(f"Key #{key}: {translated}")