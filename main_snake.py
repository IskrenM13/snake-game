from turtle import *
import time
from snake import Snake
from food import Food

from scoreboard import ScoreBoard
screen = Screen()
screen.setup(width=600, height=600)
screen.bgpic("backgrsn.gif")
screen.title("Super snake")
screen.tracer(0)
snake = Snake()
food = Food()
scoreboard = ScoreBoard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.15)
    snake.move()
    sleep=0.15
    if snake.segments[0].distance(food) < 15:
        food.refresh()
        scoreboard.score += 1
        scoreboard.score_up()
        snake.extend()
        if scoreboard.score%10 == 0:
            sleep -= 0.02
            time.sleep(sleep)

    if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -280 or snake.segments[0].ycor() > 280 or snake.segments[0].ycor() < -280:
        scoreboard.highscore()
        snake.reset()
        time.sleep(0.5)
    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 10:
            scoreboard.highscore()
            snake.reset()
            time.sleep(0.5)




screen.exitonclick()