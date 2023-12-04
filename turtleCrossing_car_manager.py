from turtle import Turtle
import random

COLORS = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class Car_manager():
    def __init__(self):
        self.all_cars =[]

    def create_car(self):
        new_car = Turtle('square')
        new_car.penup()
        new_car.shapesize(stretch_len=1, stretch_wid=2)
        new_car.color(random.choice(COLORS))

        random_y_range = random.randint(-250, 250)
        new_car.goto(300, random_y_range)
        self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)
        