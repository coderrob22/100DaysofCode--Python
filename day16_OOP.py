from turtle import Turtle, Screen
import prettytable

# turner = Turtle()
#
# my_screen = Screen()
#
# my_screen.canvheight
# turner.shape("turtle")
# turner.color("cyan")
# turner.fd(100)
#
# print(my_screen)
# my_screen.exitonclick()

table = prettytable.PrettyTable()

table.add_column("Pokemon_Name", ["Pikachu", "Squirtle", "Charmander"])

print(table)