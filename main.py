# CREATING SNAKE GAME

# Steps:
# 1. Create Snake Body
# 2. Move the Snake
# 3. Control the Snake
# 4. Detect Collision with Food
# 5. Create a Scoreboard
# 6. Detect Collision with Wall
# 7. Detect Collision with Tail


from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(height=600, width=600)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)  # stopping the turtle animation so that our turtle can move without any jitters

snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
is_game_on = True
while is_game_on:
    screen.update()  # updating turtle animation back on after creating segments
    time.sleep(0.1)  # delaying screen for 0.1 seconds
    snake.move()

    # Detecting collision with food
    if snake.head.distance(food) < 15:
        food.new_location()
        snake.extend_segment()
        score.increase_score()

    # Detecting collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 300 or snake.head.ycor() < -280:
        score.reset_score()
        snake.reset_snake()

    # Detecting collision with tail
    for segment in snake.no_of_segments[1:]:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            score.reset_score()
            snake.reset_snake()
screen.exitonclick()
