from turtle import Screen, Turtle
from Snake_Body import Snake
from Food import Food
from ScoreBoard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Welcome To The Snake Game...")
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(snake.right, "Right")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")

Game_On = True

while Game_On:
    screen.update()
    time.sleep(0.11)
    snake.move()

    #This is for food touch
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.score_increase()

    #This is for boundary touch
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.game_result()
        Game_On = False

    #This is for Tail touch
    for each in snake.snakes:
        if each == snake.head:
            pass
        elif snake.head.distance(each) < 10:
            score.game_result()
            Game_On = False


screen.exitonclick()