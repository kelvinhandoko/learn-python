from turtle import Turtle, Screen
import random

my_screen = Screen()
my_screen.setup(width=500, height=500)
user_bet = my_screen.textinput(title="enter your bet", prompt="which turtle win the race. Enter the color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
is_race_on = False
y_coor = -210
all_turtle = []

for color in colors:
    tim = Turtle(shape="turtle")
    tim.speed(3)
    tim.penup()
    tim.color(color)
    tim.goto(-230, y_coor)
    all_turtle.append(tim)
    y_coor += 80

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"you've won! the {winning_color} turtle win the race!!!")
            else:
                print(f"you've lose! the {winning_color} turtle win the race!!!")
        else:
            rand_dist = random.randint(0, 10)
            turtle.forward(rand_dist)

my_screen.exitonclick()
