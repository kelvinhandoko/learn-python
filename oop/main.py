from turtle import Screen, Turtle

timmy = Turtle()
timmy.color("red", "yellow")
timmy.begin_fill()
while True:
    timmy.forward(200)
    timmy.left(170)
    if abs(timmy.pos()) < 1:
        break
timmy.end_fill()
timmy.done()

# my_screen = Screen()
# my_screen.exitonclick()
