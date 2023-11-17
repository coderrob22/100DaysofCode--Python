from turtle import Screen
from pong_paddle import Paddle
from pong_ball import Ball
import time
from pong_scoreboard import Scoreboard

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

# Score
score = Scoreboard()


screen.listen()
screen.onkey(right_paddle.go_up, 'Up')
screen.onkey(right_paddle.go_down, 'Down')
screen.onkey(left_paddle.go_up, 'w')
screen.onkey(left_paddle.go_down, 's')

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect ball collision with the top or bottom walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.wall_bounce()
        
    # Detect ball collision with the paddles
    if ball.distance(right_paddle) < 50 and ball.xcor() > 325:
        ball.paddle_bounce()
    if ball.distance(left_paddle) < 50 and ball.xcor() < -325:
        ball.paddle_bounce()

    # Detect if ball goes out of bounds
    # # If right paddle misses the ball
    if ball.xcor() > 390 :
        ball.ball_reset()
        score.plus_left()
    
    # #If left paddle misses the ball
    if ball.xcor() < -390:
        ball.ball_reset()
        score.plus_right()

screen.exitonclick()