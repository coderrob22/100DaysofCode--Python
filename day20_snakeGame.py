from turtle import Screen
import time
from snake_game_snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My Snake Game')

# Turn off tracer to stop the un-snakelike movement
screen.tracer(0)

snake = Snake()

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

    
screen.exitonclick()