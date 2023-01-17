def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def turn_around():
    turn_left()
    turn_left()
    
def make_a_square():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_right()
    move()

def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()
    

# Shell functions that are built into the program below
def turn_left():
    pass
def move():
    pass
def at_goal():
    pass
def front_is_clear():
    pass
def wall_in_front():
    pass
def wall_on_right():
    pass