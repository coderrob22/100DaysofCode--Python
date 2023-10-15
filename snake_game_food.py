from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('cirlce')
        self.penup()
        self.shapesize(stretch_len=.5, stretch_wid=.5)
        self.color('blue')
        self.speed('fastest')
        y_coordinate = random.randint(-280, 280)
        x_coordinate = random.randint(-280, 280)
        self.goto(x_coordinate, y_coordinate)