import random
from turtle import Screen, Turtle

colors = [
    "#404258",
    "#474E68",
    "#50577A",
    "#6B728E",
    "#2A0944",
    "#3FA796",
    "#FEC260",
    "#A10035",
]
direction = [0, 90, 180, 270]
tim = Turtle()
tim.speed(3)
tim.pensize(10)
my_screen = Screen()
for i in range(200):
    tim.forward(25)
    tim.color(random.choice(colors))
    tim.setheading(random.choice(direction))

my_screen.exitonclick()
