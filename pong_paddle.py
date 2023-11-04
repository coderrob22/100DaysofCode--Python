from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.create_paddle()
    
    def create_paddle(self):
        self.shape('square')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color('white')
        self.penup()

    def starting_coordinate(self):
        self.goto(350, 0)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)