import random
from turtle import Turtle, Screen, colormode

colormode(255)


def rgb_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


tim = Turtle()
my_screen = Screen()
tim.speed("fastest")


def spiro_graph(gap):
    for _ in range(round(360 / gap)):
        tim.circle(100)
        tim.color(rgb_color())
        tim.setheading(tim.heading() + gap)


spiro_graph(2)
my_screen.exitonclick()
