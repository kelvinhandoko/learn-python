from turtle import Turtle, Screen

tim = Turtle()
my_screen = Screen()
colors = [
    "#9A1663",
    "#E0144C",
    "#FF5858",
    "#FF97C1",
]
tim.shape("turtle")


def draw_shape(sides):
    for i in range(sides):
        tim.color(colors[i % len(colors)])
        angle = 360 / sides
        tim.forward(100)
        tim.right(angle)


for i in range(7, 15):
    draw_shape(i)
my_screen.exitonclick()
