from day16_coffee_menu_data import Menu, MenuItem
from day16_coffee_maker_data import CoffeeMaker
from day16_coffee_money_machine import MoneyMachine

# Create objects from the Classes that have been imported
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
#menu_item = MenuItem()

is_on = True
choice = input(f"What kind of coffee would you like? Type {menu.get_items()} ")

while is_on:
    if choice == 'report':
        coffee_maker.report()
        money_machine.report()
    elif choice == 'off':
        print("Machine is shutting down...")
        is_on = False
    else:
        drink = menu.find_drink(choice)