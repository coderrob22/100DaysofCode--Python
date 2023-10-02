from turtle import Turtle, Screen


screen = Screen()
screen.setup(width=500, height=400)
user_guess = screen.textinput(title='Make a Bet!', prompt='Who will win the race')
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

tim = Turtle(shape='turtle')
tim.penup()
tim.goto(-230, 0)

ben = Turtle(shape='turtle')
ben.penup()
ben.goto(-230, 20)

kim = Turtle(shape='turtle')
kim.penup()
kim.goto(-230, -20)

jill = Turtle(shape='turtle')
jill.penup()
jill.goto(-230, 40)

steve = Turtle(shape='turtle')
steve.penup()
steve.goto(-230, -40)

jack = Turtle(shape='turtle')
jack.penup()
jack.goto(-230, 60)





screen.exitonclick()