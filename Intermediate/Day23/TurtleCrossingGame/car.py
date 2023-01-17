from turtle import Turtle
import random

STARTING_MOVE_SPEED = 5

color_list = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

MOVE_INCREMENT = 5

class CarManager():
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_SPEED

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle('square')
            new_car.color(random.choice(color_list))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.setx(420)
            new_car.sety(random.randint(-200, 200))
            self.all_cars.append(new_car)

    def move_cars(self):
        for cur_car in self.all_cars:
            cur_car.backward(self.car_speed)
    
    def next_level(self):
        self.car_speed += MOVE_INCREMENT