#Project 15 Deep Cave:

"""This program is an animation of a deep cave that descends forever into the earth.
Although short, this program takes advantage of the scrolling nature of the computer
screen to produce an interesting and unending visualization, proof that it doesn’t
take much code to produce something fun to watch. This program is similar to
Project 58, “Rainbow.”"""

#importing the needed modules:
import random, sys, time

#setting up the constants:
width = 70
pause_amount = 0.05
border = "*"

print("You are climbing down a deeeeeep, deeeeep cave...")
print("Press Ctrl + C to stop climbing")
time.sleep(2)

left_width = 20
gap_width = 10

while True:
    #displaying the tunnel segment:
    right_width = width - gap_width - left_width
    print((border * left_width) + (" " * gap_width) + (border * right_width))
    with open("cave.txt", "a") as cave:
        cave.write(f"{border*left_width}{' '*gap_width}{border*right_width}\n")

    #checking for Ctrl + C press during the brief pause. If it was pressed, close the program:
    try:
        time.sleep(pause_amount)
    except KeyboardInterrupt:
        print("Program will be aborted.")
        sys.exit()
    

    #adjusting the left side width:
    dice_roll = random.randint(1, 6)
    if dice_roll == 1 and left_width > 1:
        left_width -= 1
    elif dice_roll == 2 and left_width + gap_width < width -1:
        left_width += 1
    else:
        pass
