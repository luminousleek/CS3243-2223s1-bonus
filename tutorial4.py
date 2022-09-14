from itertools import product
import copy

coord_grid = list(product(range(3), range(3)))

# Coordinate system
#    x
#    0 1 2
# y 0
#   1
#   2

inital_state_3a = [
    [2,3,None],
    [1,8,4],
    [7,6,5]
]

inital_state_3b = [
    [2,3,None],
    [1,7,4],
    [8,6,5]
]

goal_state = [
    [1,2,3],
    [8,None,4],
    [7,6,5]
]

def print_state(s, name):
    print(name)
    pretty_s = ''
    for y in range(3):
        for x in range(3):
            if s[y][x]:
                pretty_s += str(s[y][x])
            else:
                pretty_s += "X"
            pretty_s += " "
        pretty_s += "\n"
    print(pretty_s)

print_state(inital_state_3a, "inital_state_3a")
print_state(goal_state, "goal_state")

def f(s):
    mismatched_tiles = 0
    for y, x in coord_grid:
        if s[y][x] == None:
          continue
        if s[y][x] != goal_state[y][x]:
          mismatched_tiles += 1
    return mismatched_tiles

# Returns the coordinate of the empty piece
def find_empty_coord(s):
    for y, x in coord_grid:
        if s[y][x] == None:
            return (x,y)

# UP, DOWN, LEFT, RIGHT
# Calculate the new coord of the empty piece after transition
transition_coord_fns = [
    lambda x,y: (x,y-1),
    lambda x,y: (x,y+1),
    lambda x,y: (x-1,y),
    lambda x,y: (x+1,y)
]

# Returns the 4 possible successor states in this sequence, UP, DOWN, LEFT, RIGHT
# If the successor states are invalid, return None.
def transition_fn(s):
    successor_states = []
    empty_coord = find_empty_coord(s)
    old_x, old_y = empty_coord
    for transition_coord_fn in transition_coord_fns:
        successor_empty_coord = transition_coord_fn(*empty_coord)
        if all([ 0<=c and c<=2  for c in successor_empty_coord]):
            successor_s = copy.deepcopy(s)
            new_x, new_y = successor_empty_coord
            # replace old blank square with new value
            successor_s[old_y][old_x] = s[new_y][new_x]
            # replace old value square with blank square
            successor_s[new_y][new_x] = None
            successor_states.append(successor_s)
        else:
            successor_states.append(None)
    return successor_states

# Check your impl so far
print(f"f(inital_3a) = {f(inital_state_3a)}")
seq_names = ["UP", "DOWN", "LEFT", "RIGHT"]
for succ_s, seq_name in zip(transition_fn(inital_state_3a), seq_names):
    if succ_s:
        print_state(succ_s, f"inital_3a, {seq_name}, f={f(succ_s)}")

# Print the trace, like below.
'''
========== Hill Climbing 3a ==========
DOWN, f=5
2 3 4 
1 8 X 
7 6 5 

LEFT, f=3
2 X 3 
1 8 4 
7 6 5 

--------------------
'''

# Now we solve 3a using code
def hill_climbing(inital_state):
    curr = inital_state
    print_state(curr, f"initial state, f={f(curr)}")
    while True:
      successors = transition_fn(curr)
      states_costs = [(state, f(state)) for state in successors if state is not None]
      next = min(states_costs, key=lambda tup: tup[1])[0]
      if f(curr) < f(next): return curr
      if f(next) == 0: return next
      curr = next
      print_state(curr, f"intermediate state, f={f(curr)}")

print("========== Hill Climbing 3a ==========")
minima_state = hill_climbing(inital_state_3a)
print_state(minima_state, f"minima_state 3a, f={f(minima_state)}")

print("========== Hill Climbing 3b ==========")
minima_state = hill_climbing(inital_state_3b)
print_state(minima_state, f"minima_state 3b, f={f(minima_state)}")