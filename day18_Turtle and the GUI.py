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

for _ in range(5):    
    tim.forward(10)
    tim.up()
    tim.forward(10)
    tim.down()


screen = Screen()
screen.exitonclick()