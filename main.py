import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

s = Screen()
s.setup(width=600, height=600)
s.bgcolor("black")
s.title("Snake (2/2) - Sinclair)")
s.tracer(0)

scoreboard = Scoreboard()
snake = Snake()
food = Food()


def start():
    go = s.textinput("Snake (2/2) - Sinclair", "Welcome to 'snake'.\n"
                                               "Movement with arrow-keys (↕/↔)\n\n"
                                               "Type: 'go' to start!\n"
                                               "\n RULES: \nYou're not allowed to touch your tail or walls.").lower()
    if go != "go":
        start()


start()

s.listen()
s.onkey(snake.up, "Up")
s.onkey(snake.down, "Down")
s.onkey(snake.left, "Left")
s.onkey(snake.right, "Right")

game_over = False

while not game_over:
    s.update()
    time.sleep(0.1)
    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.add()
        snake.extend()

    # detect collision with wall
    if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() > 295 or snake.head.ycor() < -295:
        scoreboard.reset_score()
        snake.reset_snake()

    # detect collision with tail
    for i in snake.snakes[1::]:
        if snake.head.distance(i) < 10:
            scoreboard.reset_score()
            snake.reset_snake()

s.exitonclick()
