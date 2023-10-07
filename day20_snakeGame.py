from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My Snake Game')

# Turn off tracer to stop the un-snakelike movement
screen.tracer(0)

starting_postions = [(0,0), (-20, 0), (-40, 0)]

segments =[]

# Create the Snake body for the game
for position in starting_postions:
    snake = Turtle('square')
    snake.color('white')
    snake.penup()
    snake.goto(position)
    segments.append(snake)

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

# Move the Snake around
    for seg_num in range(len(segments) - 1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()

        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20)

    
screen.exitonclick()