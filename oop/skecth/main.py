from turtle import Turtle, Screen

tim = Turtle()
my_screen = Screen()


def move_forward():
    tim.forward(10)


def move_up():
    tim.setheading(90)
    move_forward()


def move_right():
    tim.setheading(0)
    move_forward()


def move_left():
    tim.setheading(180)
    move_forward()


def move_down():
    tim.setheading(270)
    move_forward()


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


my_screen.listen()
my_screen.onkey(key="space", fun=move_forward)
my_screen.onkey(key="Up", fun=move_up)
my_screen.onkey(key="w", fun=move_up)
my_screen.onkey(key="Right", fun=move_right)
my_screen.onkey(key="d", fun=move_right)
my_screen.onkey(key="Left", fun=move_left)
my_screen.onkey(key="a", fun=move_left)
my_screen.onkey(key="Down", fun=move_down)
my_screen.onkey(key="s", fun=move_down)
my_screen.onkey(key="c", fun=clear)
my_screen.exitonclick()
