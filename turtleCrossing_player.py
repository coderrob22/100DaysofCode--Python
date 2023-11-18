from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('black')
        self.penup()
        self.goto(STARTING_POSITION)
        self.left(90)

    def Move_up(self):
        # new_y = self.ycor() + MOVE_DISTANCE
        # self.goto(self.xcor(), new_y)

        # refactored to a simple forward()
        self.forward(MOVE_DISTANCE)