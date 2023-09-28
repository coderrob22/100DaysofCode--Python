from turtle import Turtle, Screen, colormode
import random

tim = Turtle()

# tim.shape('turtle')
# tim.color('gold')
# tim.forward(100)
# tim.right(90)

#Draw a square

# for _ in range(4):
#     tim.forward(100)
#     tim.left(90)

# for _ in range(5):    
#     tim.forward(10)
#     tim.up()
#     tim.forward(10)
#     tim.down()

#You must update the color mode and bring in the 'colormode' object into the module to change colors.
colormode(255)

def color_turtle():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r,g,b)


angle = [0, 90, 180, 270]

tim.pensize(5)
tim.speed(5)

for _ in range(300):
    tim.color(color_turtle())
    tim.forward(random.randint(1, 20))
    tim.setheading(random.choice(angle))

screen = Screen()
screen.exitonclick()