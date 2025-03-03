def turnright():
    turn_left()
    turn_left()
    turn_left()

  

while not at_goal():
    if wall_in_front():
        turn_left()
        move()
      
        
    elif wall_on_right():
        move()
    elif right_is_clear():
        turnright()
        move()
        turnright()
        move()
        turn_left()
    elif front_is_clear():
        move()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
