import library as l

while l.front_is_clear():
    l.move()
l.turn_left()

while not l.at_goal():
    if l.right_is_clear():
        l.library.turn_right()
        l.move()
    elif l.front_is_clear():
        l.move()
    elif l.wall_in_front():
        l.turn_left()
    elif l.wall_on_right():
        l.move()