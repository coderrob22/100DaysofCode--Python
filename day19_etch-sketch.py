from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

# FUNCTIONS FOR EVENT LISTENERS TO LISTEN FOR
def move_forward():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def turn_counter_clock():
    tim.left(10)

def turn_clockwise():
    tim.right(10)

def clear_screen():
    tim.clear()

screen.listen()

# Event listeners
screen.onkey(move_forward, 'w')
screen.onkey(move_backwards, 's')
screen.onkey(turn_counter_clock, 'a')
screen.onkey(turn_clockwise, 'd')
screen.onkey(clear_screen, 'c')

screen.exitonclick()