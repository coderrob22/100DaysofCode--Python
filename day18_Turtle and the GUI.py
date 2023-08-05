from turtle import Turtle, Screen

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

def draw_shape(num_sides):
    angle = 360/num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)

for shape_side_n in range(3, 11):
    draw_shape(shape_side_n)

screen = Screen()
screen.exitonclick()