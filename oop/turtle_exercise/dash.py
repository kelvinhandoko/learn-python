from turtle import Turtle, Screen, color

tim = Turtle()
my_screen = Screen()
for i in range(10):
    tim.dot()
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()

my_screen.exitonclick()
