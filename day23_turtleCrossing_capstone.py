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
car_manager = Car_manager()


# Event Listeners
screen.listen()
screen.onkey(player.Move_up, "Up")


game_is_on = True

while game_is_on:
    time.sleep(.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # Detect when player collides into car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False

    # Detect when turtle crosses to the other side
    if player.arrived_at_finish_line():
        player.go_to_start()

screen.exitonclick()