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

def draw_shape(num_sides):
    angle = 360/num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)

for shape_side_n in range(3, 11):
    tim.color(random.choice(colors))
    draw_shape(shape_side_n)

screen = Screen()
screen.exitonclick()