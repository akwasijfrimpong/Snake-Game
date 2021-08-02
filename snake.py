from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]


    def add(self, position):
        body = Turtle('square')
        body.color('red')
        body.penup()
        body.goto(position)
        self.snake.append(body)


    def create_snake(self):
        x= 0
        y = 0
        for i in range(3):
            self.add((x, y))
            x-=20

    def extend(self):
        self.add(self.snake[len(self.snake)-1].position())


    def move(self):

        for part in range(len(self.snake) - 1, -1, -1):
            if part == 0:
                self.snake[part].forward(MOVE_DISTANCE)
            else:
                self.snake[part].goto(self.snake[part - 1].xcor(), self.snake[part - 1].ycor())

    def up(self):

        if self.head.heading() != DOWN:
            self.snake[0].setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.snake[0].setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.snake[0].setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.snake[0].setheading(RIGHT)
    def reset(self):
        for i in self.snake:
            i.goto(1000,1000)
        self.snake.clear()
        self.create_snake()
        self.head = self.snake[0]