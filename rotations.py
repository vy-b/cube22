import copy
def facet_1_5(state, facet, clockwise=True):
  # create deepcopy to ensure initial state does not change
  newstate = copy.deepcopy(state)
  if (facet == 1 and clockwise) or (facet == 5 and not clockwise):
    newstate[0][1] = state[0][0]
    newstate[0][0] = state[0][2]
    newstate[0][2] = state[0][3]
    newstate[0][3] = state[0][1]
    newstate[1][0] = state[2][0]
    newstate[1][1] = state[2][1]
    newstate[2][0] = state[3][0]
    newstate[2][1] = state[3][1]
    newstate[3][0] = state[5][3]
    newstate[3][1] = state[5][2]
    newstate[5][3] = state[1][0]
    newstate[5][2] = state[1][1]
  elif (facet == 5 and clockwise) or (facet == 1 and not clockwise):
    newstate[0][0] = state[0][1]
    newstate[0][2] = state[0][0]
    newstate[0][3] = state[0][2]
    newstate[0][1] = state[0][3]
    newstate[2][0] = state[1][0]
    newstate[2][1] = state[1][1]
    newstate[3][0] = state[2][0]
    newstate[3][1] = state[2][1]
    newstate[5][3] = state[3][0]
    newstate[5][2] = state[3][1]
    newstate[1][0] = state[5][3]
    newstate[1][1] = state[5][2]
  else:
    print("invalid facet number called")
    return None

  
  # print("turn facet "+str(facet)+" "+move,end="\n")
  return newstate


def facet_2_4(state, facet, clockwise=True):
  newstate = copy.deepcopy(state)

  if (facet == 2 and clockwise) or (facet == 4 and not clockwise):
    edges = [0, 2]
    faces = [0, 5, 4, 2]
    newstate[1][1] = state[1][0]
    newstate[1][0] = state[1][2]
    newstate[1][2] = state[1][3]
    newstate[1][3] = state[1][1]
    newstate[0][0] = state[5][0]
    newstate[0][2] = state[5][2]
    newstate[2][0] = state[0][0]
    newstate[2][2] = state[0][2]
    newstate[4][0] = state[2][0]
    newstate[4][2] = state[2][2]
    newstate[5][0] = state[4][0]
    newstate[5][2] = state[4][2]

  elif (facet == 4 and clockwise) or (facet == 2 and not clockwise):
    newstate[1][0] = state[1][1]
    newstate[1][2] = state[1][0]
    newstate[1][3] = state[1][2]
    newstate[1][1] = state[1][3]
    newstate[5][0] = state[0][0]
    newstate[5][2] = state[0][2]
    newstate[0][0] = state[2][0]
    newstate[0][2] = state[2][2]
    newstate[2][0] = state[4][0]
    newstate[2][2] = state[4][2]
    newstate[4][0] = state[5][0]
    newstate[4][2] = state[5][2]
  # print("turn facet "+str(facet)+" "+move,end="\n")
  return newstate


def facet_3_6(state, facet, clockwise=True):
  # create deepcopy to ensure initial state does not change
  newstate = copy.deepcopy(state)
  if (facet == 3 and clockwise) or (facet == 6 and not clockwise):
    newstate[2][1] = state[2][0]
    newstate[2][0] = state[2][2]
    newstate[2][2] = state[2][3]
    newstate[2][3] = state[2][1]
    newstate[0][3] = state[1][1]
    newstate[0][2] = state[1][3]
    newstate[3][0] = state[0][2]
    newstate[3][2] = state[0][3]
    newstate[4][0] = state[3][2]
    newstate[4][1] = state[3][0]
    newstate[1][1] = state[4][0]
    newstate[1][3] = state[4][1]
  elif (facet == 6 and clockwise) or (facet == 3 and not clockwise):
    newstate[2][0] = state[2][1]
    newstate[2][2] = state[2][0]
    newstate[2][3] = state[2][2]
    newstate[2][1] = state[2][3]
    newstate[1][1] = state[0][3]
    newstate[1][3] = state[0][2]
    newstate[0][2] = state[3][0]
    newstate[0][3] = state[3][2]
    newstate[3][2] = state[4][0]
    newstate[3][0] = state[4][1]
    newstate[4][0] = state[1][1]
    newstate[4][1] = state[1][3]
  # print("turn facet "+str(facet)+" "+move,end="\n")
  return newstate