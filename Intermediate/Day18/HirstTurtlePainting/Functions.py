import random
import colorgram
import random
from turtle import Turtle, Screen, colormode

rgb_colors = []
def extract_colors(file : str):
    colors = colorgram.extract(file, 30)
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        new_color = (r, g, b)
        rgb_colors.append(new_color)
    return rgb_colors

def gen_ran_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0, 255)
    tpl = (r, g , b)
    return tpl


def draw_stupid_art(height_list, width_list):
    colormode(255)
    timmy = Turtle()
    timmy.shape('turtle')
    timmy.penup()
    for y in height_list:
        timmy.sety(y)
        for x in width_list:
            timmy.setx(x)
            timmy.pencolor(random.choice(rgb_colors))
            timmy.dot(20)
    
    screen = Screen()
    screen.colormode(255)
    screen.exitonclick()
