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

numberofjumps = 6
while numberofjumps > 0:
    thisone()
    numberofjumps -= 1
    print(numberofjumps)
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
