from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('green')
screen.title("Snake")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score(0)
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

flag = True
track = 0
while  flag:
    screen.update()
    time.sleep(0.08)

    snake.move()
    if snake.head.distance(food) < 15:
        track += 1
        score.update_score(track)
        food.change_location()
        snake.extend()
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        score.reset(track)
        snake.reset()
    for body in snake.snake[1:]:

        if snake.head.distance(body)<10:
            score.reset(track)
            snake.reset()





screen.exitonclick()
