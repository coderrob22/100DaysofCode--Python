from turtle import Screen
import time
from turtleCrossing_player import Player
from turtleCrossing_car_manager import Car_manager
from turtle_crossing_scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Call the classes
player = Player()


# Event Listeners
screen.listen()
screen.onkey(player.Move_up, "Up")


game_is_on = True

while game_is_on:
    time.sleep(.1)
    screen.update()

