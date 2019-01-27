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
    open_states = grid.copy()
    # set the first initial state to closed
    open_states[init[0]][init[1]] = 1
    return find_next_neighbours(0, 0, open_states)
    
    
    
    return open_states
def find_next_neighbours(y, x, open_states):
    neighbours = []
    # loop through all the directions
    for i in range(len(delta)):
        # next coordinate after the move
        n_y = y + delta[i][0]  
        n_x = x + delta[i][1]
        # check if we're out of bounds 
        if (n_y > len(open_states) or n_y < 0) or (n_x > len(open_states[0]) or n_x < 0):
            # skip this iteration if we're out of bounds
            continue
        if open_states[n_y][n_x] == 0:
            neighbours.append([n_y, n_x])
            open_states[n_y][n_x] = 1
    # return all the possible neighbours of the given cell
    return neighbours
