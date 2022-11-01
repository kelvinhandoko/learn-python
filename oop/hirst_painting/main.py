import random
from turtle import Turtle, Screen, colormode
import turtle
import colorgram

tim = Turtle()
my_screen = Screen()
colors = colorgram.extract("DgTrUlDUwAMl9yJ.jpeg", 30)
rgb_color = []
turtle.colormode(255)

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_color.append((r, g, b))
tim.penup()
tim.speed(8)
tim.setheading(210)
tim.forward(300)
tim.setheading(0)
tim.hideturtle()


def hirst_drawing(w, h, size, gap):
    for i in range(h):
        for _ in range(w):
            tim.dot(size, random.choice(rgb_color))
            tim.forward(gap)
        if i < h - 1:
            tim.setheading(90)
            tim.forward(gap)
            tim.setheading(180)
            tim.forward(w * gap)
            tim.setheading(0)
        else:
            tim.setheading(180)
            tim.forward(gap)


hirst_drawing(10, 10, 20, 50)
my_screen.exitonclick()
