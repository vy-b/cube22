from util import Node, PriorityQueue, memoize
from rotations import facet_1_5,facet_2_4,facet_3_6
import copy
import random
import itertools
import time
# Vy Bui -301386690
# store state as a list
solved = [[2, 2, 2, 2],
          [6, 6, 6, 6],
          [5, 5, 5, 5],
          [3, 3, 3, 3],
          [4, 4, 4, 4],
          [1, 1, 1, 1]]
example = [[4, 4, 2, 2], 
          [1, 3, 5, 6], 
          [1, 1, 5, 5], 
          [6, 3, 6, 3], 
          [4, 2, 2, 4],
          [3, 1, 6, 5]]
def main():
  # testing example in q4 - time is approx 45s-1min
  newCube = Cube(example)
  print("cube colors:")
  display(newCube.initial)
  print("heuristic:",newCube.h(Node(newCube.initial)))
  h=memoize(newCube.h,'h')
  start_time = time.time()
  best_first_graph_search(newCube, lambda n: n.path_cost + h(n))
  end_time = time.time()
  elapsed = end_time - start_time
  print("time taken: ",elapsed)

  # testing random example - shuffled 15 times
  newCube = Cube(solved)
  newCube.shuffle(15)
  print("cube colors:")
  display(newCube.initial)
  print("heuristic:",newCube.h(Node(newCube.initial)))
  h=memoize(newCube.h,'h')
  start_time = time.time()
  best_first_graph_search(newCube, lambda n: n.path_cost + h(n))
  end_time = time.time()
  elapsed = end_time - start_time
  print("time taken: ",elapsed)



class Cube:
  def __init__(self, initial):
    self.initial = initial

  def shuffle(self,n):
    # randomly shuffles cube
    shuffle_cube = random.choices(self.actions(), k=n)
    for i in shuffle_cube:
      self.initial = self.next_state(self.initial,i)
    
  def actions(self):
    return [[1,True],[1,False],[2,True],[2,False],[3,True],[3,False],[4,True],[4,False],[5,True],[5,False],[6,True],[6,False]]
    
  def next_state(self,state,action):
    # outputs the next state from the current state after carrying out the action specified
    facet = action[0]
    clockwise = action[1]
    if (facet == 1 or facet == 5):
      return facet_1_5(state,facet,clockwise)
    elif (facet == 3 or facet == 6):
      return facet_3_6(state,facet,clockwise)
    elif (facet == 2 or facet == 4):
      return facet_2_4(state,facet,clockwise)

  def path_cost(self, c, state1, action, state2):
        return c + 1

  def goal_test(self, state):
    possible_goals = list(itertools.permutations(solved))
    return tuple(state) in possible_goals
                      
  def h(self,node):
    sum_4_diff = 0
    sum_3_diff = 0
    sum_2_diff = 0
    for i in range(len(node.state)):
      unique = len(set(node.state[i]))
      if (unique == 4):
        sum_4_diff+=1
      elif (unique==3):
        sum_3_diff+=1
      elif(unique==2):
        sum_2_diff+=1
    return 4*sum_4_diff+2*sum_3_diff+sum_2_diff

# Displays current state of cube
def display(state):
  for i in range(len(state)):
    for j in range(len(state[i])):
      if (j==3):
        temp="\n"
      else:
        temp=" "
      print(state[i][j],end=temp)
  print("\n")


# Taken from q3 best_first_graph_search with modifications to adapt to cube
def best_first_graph_search(problem, f, display=True):
    """Search the nodes with the lowest f scores first.
    You specify the function f(node) that you want to minimize; for example,
    if f is a heuristic estimate to the goal, then we have greedy best
    first search; if f is node.depth then we have breadth-first search.
    There is a subtlety: the line "f = memoize(f, 'f')" means that the f
    values will be cached on the nodes as they are computed. So after doing
    a best first search you can examine the f values of the path returned."""
    f = memoize(f, 'f')
    
    node = Node(problem.initial)
    frontier = PriorityQueue('min', f)
    frontier.append(node)
    explored = set()
    while frontier:
        node = frontier.pop()
        if problem.goal_test(node.state):
            if display:
              print(node.state)
              print("Produced Nodes: ",len(explored)+len(frontier))
              print("Expanded Nodes: ",len(explored))
              print("Answer depth: ",len(node.solution()))
              print("Max memory: ",len(explored)+len(frontier))
              print("\n")
              print("Solution:")
              for i in node.solution():
                  print(i)
              print("\n")
            return node
        explored.add(str(node.state))
        for child in node.expand(problem):
            if str(child.state) not in explored and child not in frontier:
                frontier.append(child)
            elif child in frontier:
                if (f(child) < frontier[child]):
                    del frontier[child]
                    frontier.append(child)
    return None

if __name__ == "__main__":
    main()