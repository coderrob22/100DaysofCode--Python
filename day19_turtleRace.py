from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width=500, height=400)
user_guess = screen.textinput(title='Make a Bet!', prompt='Who will win the race')
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
y_coordinate = [0, 30, -30, 60, -60, 90]
all_turtles = []

for x in range(0, 6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color(colors[x])
    new_turtle.goto(x=-230, y= y_coordinate[x])
    all_turtles.append(new_turtle)

if user_guess:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()