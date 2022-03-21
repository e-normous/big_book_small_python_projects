#project 6: Caesar cipher https://inventwithpython.com/bigbookpython/project6.html

"""The Caesar cipher is an ancient encryption algorithm used by Julius Caesar.
It encrypts letters by shifting them over by a certain number of places in the alphabet.
We call the length of shift the key. For example, if the key is 3, then A
becomes D, B becomes E, C becomes F, and so on. To decrypt the message, you 
must shift the encrypted letters in the opposite direction. This program lets 
the user encrypt and decrypt messages according to this algorithm."""


#if pyperclip (which is used to copy the text to the clipboard) is installed, it's all good
try:
    import pyperclip
    print("You'll be able to copy your text to the clipboard later.")

#if pyperclip cannot be imported. raise the error or just pass respectively
except ImportError:
    print("Copying to the clipboard will not be possible.")
    pass

#defining all the possible symbols that can be encrypted/decrypted:
symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

print('Caesar Cipher, by Al Sweigart al@inventwithpython.com')
print('The Caesar cipher encrypts letters by shifting them over by a')
print('key number. For example, a key of 2 means the letter A is')
print('encrypted into C, the letter B encrypted into D, and so on.')
print()

#ask the user whether they're encrypting or decrypting:
#loop until the user enters a valid entry (and then break the loop):
while True:
    print("Do you wish tho (e)ncrypt or (d)ecrypt?")
    response = input("> ").lower()
    if response.startswith("e"):
        mode = "encrypt"
        break
    elif response.startswith("d"):
        mode = "decrypt"
        break
    print("Please enter the letter e or d.")

#Let the user enter the key to use:
#Loop until the user enters a valid key
while True:
    #the maximum key is defined by the amount of symbols:
    max_key = len(symbols) -1
    print(f"Please enter the key (0 to {max_key}) to use.")
    response = input("> ").upper()
    if not response.isdecimal():
        continue
    if 0 <= int(response) < len(symbols):
        key = int(response)
        break

#Let the user enter the message to encrypt/decrypt:
print(f"Please enter the message to {mode}.")
message = input("> ")

#Caesar cipher only works on uppercase letters:
message = message.upper()

#storing the encrypted/decrypted form of the message:
translated = ""

#Encrypt/decrypt each symbol in the message:
for symbol in message:
    if symbol in symbols:
        #get the encrypted (or decrypted) number for this symbol:
        num = symbols.find(symbol)
        if mode == "encrypt":
            num += key
        elif mode == "decrypt":
            num -= key
        
        #Handle the wrap-around if num is larger than the length of symbols or less than 0:
        if num >= len(symbols):
            num -= len(symbols)
        elif num < 0:
            num += len(symbols)

        #Add encrypted/decrypted number's symbol to "translated":
        translated += symbols[num]
    else:
        #just add the symbol without encrypting/derypting:
        translated += symbol

#Display the encrypted/decrypted string to the screen:
print(translated)

#Copy the translated text to the clipboard:
try:
    pyperclip.copy(translated)
    print(f"Full {mode}ed text copied to clipboard.")
except:
    pass
