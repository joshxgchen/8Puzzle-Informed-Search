# puzzle.py
from random import *
import time
from search import *
# ...

def make_rand_8_puzzle():

  newPuzzle = [] #create a new list to make an 8 puzzle
  for i in range (9):
    newPuzzle.append(i) #iterate and add i sequentially
  random.shuffle((newPuzzle)) #shuffle newpuzzle so it becomes randomized using random function
  tuple(newPuzzle)
  puzzle = EightPuzzle((newPuzzle))
  while(puzzle.check_solvability(newPuzzle)==False):
    random.shuffle(newPuzzle)
    puzzle = EightPuzzle(tuple(newPuzzle)) 
  return tuple(newPuzzle) #add a tuple to put them all in parentheses  

def display(state):
  newDisplay = [0,0,0,0,0,0,0,0,0]
  result = ""
  for i in range (9):
    newDisplay[i] = state[i]
    if (state[i]==0):
      newDisplay[i] = "*"
  print(newDisplay[0],newDisplay[1],newDisplay[2])
  print(newDisplay[3],newDisplay[4],newDisplay[5])
  print(newDisplay[6],newDisplay[7],newDisplay[8])


def manhattan(n):
  state = n.state
  index_goal = {0: [2, 2], 1: [0, 0], 2: [0, 1], 3: [0, 2], 4: [1, 0], 5: [1, 1], 6: [1, 2], 7: [2, 0], 8: [2, 1]}
  index_state = {}
  index = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]

  for i in range(len(state)):
    index_state[state[i]] = index[i]
  total = 0
  for i in range(8):
    for j in range(2):
      total = abs(index_goal[i][j] - index_state[i][j]) + total
  #now we're subtracting to account for 0 
  for x in range(2):
    total = total - abs(index_state[0][x] - index[0][x])
  return total


def gaschnig(n):

  moves = 0
  curr = list(n.state)
  solved = [1,2,3,4,5,6,7,8,0]
  while curr != solved:
    begin = curr.index(0)
    if solved[begin] != 0:
      saved = solved[begin]
      temp = curr.index(saved)
      curr[temp], curr[begin] = curr[begin], curr[temp]
    else:
      for i in range(len(curr) * len(curr)):
        if solved[i] != curr[i]:
          curr[i], curr[begin] = curr[begin], curr[i]
          break ##if solved does not equal to curr break
    moves+=1
  return moves


variable = tuple(make_rand_8_puzzle())

if __name__ == "__main__": ##check if shell input
  counter = 0
  start = []
  final = []
  if len(sys.argv) == 9:
    for i in range(len(sys.argv)):
      if (sys.argv[i].isdigit() == True):
        start.append(sys.argv[i]) ##append a new int 
        final.append(int(start[total]))
        total = total + 1
    
    variable = tuple(final) #change variable to tuple


display(variable)
print('\n')
variable = EightPuzzle(tuple(variable))

if (variable.check_solvability(variable.initial)==False): ##LAST check to see if input is solvable 
  print("Unsolvable. Error: exit")
  sys.exit()



start = time.time()
result = astar_search(variable)
astar_search(variable, None, True)
total_time = time.time() - start
print(f'Total time for misplaced-tiles (in seconds): {total_time} seconds!')
print("The number of tiles moved is", result.path_cost)
print('\n')

start = time.time()
astar_search(variable, manhattan, True)
total_time = time.time() - start
print(f'Total time for manhattan (in seconds): {total_time} seconds!')
print ('\n')

start = time.time()
astar_search(variable, gaschnig, True)
total_time = time.time() - start
print(f'Total time for gaschnig (in seconds): {total_time} seconds!')
 


