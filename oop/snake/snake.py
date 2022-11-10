from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        x_coor = 0
        y_coor = 0
        for i in range(3):
            tim = Turtle(shape="square")
            tim.penup()
            tim.color("white")
            tim.goto(x_coor, y_coor)
            x_coor -= MOVE_DISTANCE
            self.segments.append(tim)
            if i == 0:
                tim.color("red")

    def snake_move(self):
        for seg_index in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_index - 1].xcor()
            new_y = self.segments[seg_index - 1].ycor()
            self.segments[seg_index].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def move_up(self):
        if self.head.heading() != DOWN and self.head.xcor() > -380 or self.head.xcor() < 380:
            self.head.setheading(UP)

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def check_wall(self):
        print(self.head.xcor())
        if self.head.xcor() < -380 or self.head.xcor() > 380:
            if self.head.xcor() < 0:
                new_x = abs(self.head.xcor())
            else:
                new_x = -self.head.xcor()
            self.head.goto(new_x, self.head.ycor())
        if self.head.ycor() < -380 or self.head.ycor() > 380:
            if self.head.ycor() < 0:
                new_y = abs(self.head.ycor())
            else:
                new_y = -self.head.ycor()
            self.head.goto(self.head.xcor(), new_y)

    def add_size(self):
        x_coor = self.segments[-1].xcor()
        y_coor = self.segments[-1].ycor()
        tim = Turtle(shape="square")
        tim.penup()
        tim.color("white")
        tim.goto(x_coor, y_coor)
        self.segments.append(tim)

    def restart(self):
        for segment in self.segments:
            segment.goto(10000, 10000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
