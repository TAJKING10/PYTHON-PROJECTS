def turnright():
    turn_left()
    turn_left()
    turn_left()

  

while not at_goal():
    if right_is_clear():
        turnright()
        move()
        turnright()
        move()
    elif wall_in_front():
        turn_left()
       
      
        
    elif wall_on_right():
        move()
    elif right_is_clear():
        turnright()
        move()
        turnright()
        move()
    
    elif front_is_clear():
        move()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
