def turn_right():
    turn_left()
    turn_left()
    turn_left()
  
def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

for i in range(6):
    move()
    jump()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
