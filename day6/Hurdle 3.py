def turnright():
    turn_left()
    turn_left()
    turn_left()
def thisone():
    move()
    turn_left()
    move()
    turnright()
    move()
    turnright()
    move()
    turn_left()

numberofjumps = at_goal()
while numberofjumps == at_goal():
    thisone()
    numberofjumps -= 1
    print(numberofjumps)
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
