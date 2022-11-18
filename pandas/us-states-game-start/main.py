import turtle
import pandas

screen = turtle.Screen()
screen.title("US State Games")
image = "./pandas/us-states-game-start/blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)

guessed = []

data = pandas.read_csv("./pandas/us-states-game-start/50_states.csv")
states = data.state.tolist()

while len(guessed) < 50:
    answer_state = turtle.textinput(title=f"{len(guessed)}/50 States correct", prompt="enter the state").title()

    if answer_state == "Exit":
        missing = []
        for state in states:
            if state not in guessed:
                missing.append(state)
        missing_data = pandas.DataFrame(missing)
        missing_data.to_csv("./missing_state.csv")
        break
    if answer_state in states:
        guessed.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())
    else:
        print("error")


screen.exitonclick()
