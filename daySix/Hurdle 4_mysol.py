def turn_right():
    turn_left()
    turn_left()
    turn_left()
  
def jump():
    turn_right()
    move()
    turn_right()
    move()

def check_right():
    if wall_on_right():
        move()
    else:
        jump()

def check_front():
    if front_is_clear():
        if not is_facing_north():
            move()
        else:
            check_right()
    elif wall_in_front():
        if is_facing_north():
            check_right()
        else:
            turn_left()

while not at_goal():
        check_front()
        
    
        
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
