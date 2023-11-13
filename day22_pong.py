from turtle import Screen
from pong_paddle import Paddle
from pong_ball import Ball
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

# Paddle instance
right_paddle = Paddle((350, 0))

#2nd Paddle instance
left_paddle = Paddle((-350, 0))

# Ball
ball = Ball()


screen.listen()
screen.onkey(right_paddle.go_up, 'Up')
screen.onkey(right_paddle.go_down, 'Down')
screen.onkey(left_paddle.go_up, 'w')
screen.onkey(left_paddle.go_down, 's')

game_is_on = True

while game_is_on:
    time.sleep(.1)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
        

screen.exitonclick()