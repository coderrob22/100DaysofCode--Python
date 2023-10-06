from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My Snake Game')
starting_postions = [(0,0), (-20, 0), (-40, 0)]

for position in starting_postions:
    snake = Turtle('square')
    snake.color('white')
    snake.goto(position)
    

    
screen.exitonclick()