from turtle import Screen
import time
from snake_game_snake import Snake
from snake_game_food import Food
from snake_game_scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My Snake Game')

# Turn off tracer to stop the un-snakelike movement
screen.tracer(0)

# ---------Import Snake, Food, & Scoreboard class------------
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Create event listeners to listen to arrow input-- This is how we control the snake's movement
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()


    # Logic to detect when the snake collides with the food
    if snake.head.distance(food) < 15:
        food.refresh_food()
        snake.snake_extend()
        scoreboard.increase_score()

    # Logic to detect if the snake hits the wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()
    
screen.exitonclick()