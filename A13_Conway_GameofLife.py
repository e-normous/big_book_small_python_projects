#project #13: Conway's game of life

"""Conway’s Game of Life is a cellular automata simulation that 
follows simple rules to create interesting patterns. It was
invented by mathematician John Conway in 1970 and popularized
by Martin Gardner’s “Mathematical Games” column in Scientific
American. Today, it’s a favorite among programmers and computer
scientists, though it’s more an interesting visualization than
a true “game.” The two-dimensional board has a grid of “cells,”
each of which follows three simple rules:

Living cells with two or three neighbors stay alive in the next step of the simulation.
Dead cells with exactly three neighbors become alive in the next step of the simulation.
Any other cell dies or stays dead in the next step of the simulation.
The living or dead state of the cells in the next step of the
simulation depends entirely on their current state. The cells
don’t “remember” any older states. There is a large body of
research regarding the patterns that these simple rules produce.
Tragically, Professor Conway passed away of complications from COVID-19
in April 2020. More information about Conway’s Game of Life can be found
at https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life, and more
information about Martin Gardner at https://en.wikipedia.org/wiki/Martin_Gardner."""


import copy, random, sys, time

#setting up the constants:
width = 79
height = 20

#defining the visualization of alive and dead cells:
alive = "O"
dead = " "

# The cells and nextCells are dictionaries for the state of the game.
# Their keys are (x, y) tuples and their values are one of the ALIVE
# or DEAD values.
next_cells = {}

#putting random dead and alive cells into next_cells:

#looping over every possible column:
for x in range(width):
    #looping over every possible row:
    for y in range(height):

        #setting the cells as either alive or dead, depending on the random integer that's set:
        if random.randint(0, 1) == 0:
            next_cells[(x, y)] = alive
        else:
            next_cells[(x, y)] = dead

#main program loop:

#every single iteration of the loop is a step of the simulation:
while True:
    #first of all, separate all different iterations:
    print("\n" *50)
    #copy the defined next cells:
    cells = copy.deepcopy(next_cells)

    #print the cells on the screen:
    for y in range(height):
        for x in range(width):
            print(cells[(x, y)], end="")
        print()
    print("Press 'Ctrl + C to QUIT")

    #calculating the next step's cells based on current step's cells:
    for x in range(width):
        for y in range(height):
            #get the neighboring coordinates of x and y, even if they wrap around the edge:
            left = (x - 1) % width
            right = (x + 1) % width
            above = (y - 1) % height
            below = (y + 1) % height

            #count the number of living neighbors:
            num_neighbors = 0

            #define when a neighbor is alive:
            if cells[(left, above)] == alive:
                num_neighbors += 1
            if cells[(x, above)] == alive:
                num_neighbors += 1
            if cells[(right, above)] == alive:
                num_neighbors += 1
            if cells[(left, y)] == alive:
                num_neighbors += 1
            if cells[(right, y)] == alive:
                num_neighbors += 1
            if cells[(left, below)] == alive:
                num_neighbors += 1
            if cells[(x, below)] == alive:
                num_neighbors += 1
            if cells[(right, below)] == alive:
                num_neighbors += 1

            #set cell based on conway's game of life rules:
            if cells[(x, y)] == alive and (num_neighbors == 2 or num_neighbors == 3):
                #living cells with 2 or 3 neighbors will stay alive:
                next_cells[(x, y)] = alive
            elif cells[(x, y)] == dead and num_neighbors == 3:
                #dead cells with 3 neighbors will become alive:
                next_cells[(x, y)] = alive
            else:
                #everything else will die or stay dead:
                next_cells[(x, y)] = dead

    try:
        time.sleep(1)
    except KeyboardInterrupt:
        print("That was Conway's Game of Life. RIP Prof. Conway <3")
        sys.exit()
