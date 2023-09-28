from turtle import Turtle, Screen
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

colors = ['Red', 'Blue', 'CornflowerBlue', 'Gold', 'DarkOrchid', 'Pink', 'Violet', 'SeaGreen', 'SlateGray', 'wheat']
angle = [0, 90, 180, 270]

tim.pensize(5)
tim.speed(5)

for _ in range(300):
    tim.color(random.choice(colors))
    tim.forward(random.randint(1, 20))
    tim.setheading(random.choice(angle))

screen = Screen()
screen.exitonclick()