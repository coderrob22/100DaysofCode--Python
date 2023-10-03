from turtle import Turtle, Screen


screen = Screen()
screen.setup(width=500, height=400)
user_guess = screen.textinput(title='Make a Bet!', prompt='Who will win the race')
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
y_coordinate = [0, 30, -30, 60, -60, 90]

for x in range(0, 6):
    tim = Turtle(shape='turtle')
    tim.penup()
    tim.color(colors[x])
    tim.goto(x=-230, y= y_coordinate[x])




screen.exitonclick()