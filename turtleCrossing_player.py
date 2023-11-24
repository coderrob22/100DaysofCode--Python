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
        self.go_to_start()
        self.left(90)

    def Move_up(self):
        # new_y = self.ycor() + MOVE_DISTANCE
        # self.goto(self.xcor(), new_y)

        # refactored to a simple forward()
        self.forward(MOVE_DISTANCE)

    def arrived_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
        
    def go_to_start(self):
        """This method is used to start the turtle over at the origin for each level"""
        self.goto(STARTING_POSITION)
    