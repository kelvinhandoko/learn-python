from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 360)
        self.hideturtle()
        self.update_scoreboard()

    def increment(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"score: {self.score} high score: {self.high_score}", align="center", font=("Courier", 18, "normal"))

    def game_over(self):
        self.home()
        self.write(f"You Lose", align="center", font=("Courier", 18, "normal"))

    def restart(self):
        self.clear()
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()
