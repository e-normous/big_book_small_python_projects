#project 25: Fast draw (CowBoy Edit)
"""This program tests your reaction speed:
press ENTER as soon as you see the word DRAW.
But careful, though. Press it before DRAW
appears, and you lose. Are you the fastest
keyboard in the west?"""


import random, sys, time

#in the project by Al Sweigart, the two functions are not defined. The code there is to be found directly in the while True loop.

#Defining the draw game within a function:
def draw_game():
    print("It is high noon...")
    time.sleep(random.randint(20, 50) / 10)
    print("DRAW!")
    #get the time when "DRAW" has been made visible:
    draw_time = time.time()

    #let the user input:
    input()

    #Get the time the user took until he drew:
    time_elapsed = time.time() - draw_time
    return time_elapsed

#Define the function to get the elapsed time:
def elapsed_time(time_elapsed):
    if time_elapsed < 0.01:
        print("You drew before 'DRAW' appeared on screen. You lose.")
    elif time_elapsed > 0.3:
        time_elapsed = round(time_elapsed, 4)
        print(f"You took {time_elapsed} seconds to draw. This is too slow, Cowboy!")
    else:
        time_elapsed = round(time_elapsed, 4)
        print(f"You took {time_elapsed} seconds to draw.")
        print("Goooooddamn you are fast! You win!")

print('Fast Draw, by Al Sweigart al@inventwithpython.com')
print()
print('Time to test your reflexes and see if you are the fastest')
print('draw in the west!')
print('When you see "DRAW", you have 0.3 seconds to press Enter.')
print('But you lose if you press Enter before "DRAW" appears.')
print()
input('Press Enter to begin...')

#Make the game in an infinite loop:
while True:
    time_elapsed = draw_game()
    elapsed_time(time_elapsed)
    print("Enter QUIT to stop or just press ENTER to play again.")
    response = input("> ").upper()
    
    #if the user enters quit or... anything at all, exit the system:
    if response.upper() == "QUIT" or len(response) != 0:
        print("Thank you for playing and good bye.")
        sys.exit()