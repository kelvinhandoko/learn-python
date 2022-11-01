from turtle import Screen, Turtle

tim = Turtle()
my_screen = Screen()
tim.shape("turtle")
tim.color("peru")
# buat persegi
for i in range(4):
    tim.forward(100)
    tim.left(90)

my_screen.exitonclick()
