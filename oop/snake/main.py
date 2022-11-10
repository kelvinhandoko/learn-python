from turtle import Screen
import time
from snake import Snake
from food import Food
from score_board import ScoreBoard

screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

game_is_on = True
snake = Snake()
score_board = ScoreBoard()
food = Food()
screen.listen()
screen.onkey(key="Up", fun=snake.move_up)
screen.onkey(key="Down", fun=snake.move_down)
screen.onkey(key="Left", fun=snake.move_left)
screen.onkey(key="Right", fun=snake.move_right)


def reset():
    global game_is_on
    screen.reset()
    snake = Snake()
    score_board = ScoreBoard()
    food = Food()
    return game_is_on, snake, score_board, food


screen.onkey(key="space", fun=reset)

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.snake_move()
    snake.check_wall()
    if snake.head.distance(food) < 15:
        food.refresh()
        score_board.increment()
        snake.add_size()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score_board.restart()
            snake.restart()

print(game_is_on)
screen.exitonclick()
