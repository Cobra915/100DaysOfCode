import library as l

while not l.at_goal():
    if l.front_is_clear() == 'true':
        l.move()
    elif l.wall_in_front() == 'true':
        l.jump()