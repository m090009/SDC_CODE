# ----------
# User Instructions:
# 
# Define a function, search() that returns a list
# in the form of [optimal path length, row, col]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space

import random


grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

delta_name = ['^', '<', 'v', '>']


def search(grid,init,goal,cost):
    # ----------------------------------------
    # insert code here
    # ----------------------------------------
    # Initialize an open grid 
    closed_states = grid.copy()
    # set the first initial state to closed
    closed_states[init[0]][init[1]] = 1
    # Initializing the current state with the initial state
    init_state = [0, init[0], init[1]]

    # Goal state found status flag 
    found = False
    no_path = False
    open_cells = [init_state]

    while not found and not no_path:
        # We sort our open cells according to the g-value
        open_cells.sort()        


        # Expand cell to open neighbours
        expanded_neighbours = find_next_neighbours(init[0], init[1], closed_states)
        # Add g-value to expanded neighbours
        possible_choices = [[current_state[0] + cost, n[0], n[1]] for n in expanded_neighbours]

        # Randomly choose one of the choices
        choice = random.choice(possible_choices)

    # x = [[3,1,1], [0, 1,1], [1, 1,1], [1, 1,1], [2, 1,1]]
    # x.sort(reverse=True)
    return x


def find_next_neighbours(r, c, closed_states):
    neighbours = []
    # loop through all the directions
    for i in range(len(delta)):
        # next coordinate after the move
        n_r = r + delta[i][0]  
        n_c = c + delta[i][1]
        # check if we're out of bounds 
        if (n_r > len(closed_states) or n_r < 0) or (n_c > len(closed_states[0]) or n_c < 0):
            # skip this iteration if we're out of bounds
            continue
        if closed_states[n_r][n_c] == 0:
            neighbours.append([n_r, n_c])
            closed_states[n_r][n_c] = 1
    # return all the possible neighbours of the given cell
    return neighbours

print(search(grid, init, goal, cost))