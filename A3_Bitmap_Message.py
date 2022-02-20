#A 3. Bitmap Message (https://inventwithpython.com/bigbookpython/project3.html):

#import the sys library:
import sys

#There are 68 periods along the top and bottom of this string
# and it has been copied from "inventwithpython.com/bitmapworld.txt":

bitmap = """
....................................................................
   **************   *  *** **  *      ******************************
  ********************* ** ** *  * ****************************** *
 **      *****************       ******************************
          *************          **  * **** ** ************** *
           *********            *******   **************** * *
            ********           ***************************  *
   *        * **** ***         *************** ******  ** *
               ****  *         ***************   *** ***  *
                 ******         *************    **   **  *
                 ********        *************    *  ** ***
                   ********         ********          * *** ****
                   *********         ******  *        **** ** * **
                   *********         ****** * *           *** *   *
                     ******          ***** **             *****   *
                     *****            **** *            ********
                    *****             ****              *********
                    ****              **                 *******   *
                    ***                                       *    *
                    **     *                    *
...................................................................."""

print("Bitmap Message")
print("Enter the message to display with the bitmap.")
message = input("> ")

#If the user enters an empty message, exit the program:
if message == "":
    sys.exit()

#looping over each line in the bitmap:
for line in bitmap.splitlines():
    #loop over each charcter in the line:
    for i, bit in enumerate(line):
        if bit == " ":
            #print an empty space since there's a space in the bitmap:
            print(" ", end="")
        else:
            #print a character from the user message:
            print(message[i % len(message)], end="")
            
    #printing a new line:
    print()

