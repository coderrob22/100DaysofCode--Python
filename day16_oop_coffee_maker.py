from day16_coffee_menu_data import Menu, MenuItem
from day16_coffee_maker_data import CoffeeMaker
from day16_coffee_money_machine import MoneyMachine

# Create objects from the Classes that have been imported
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
#menu_item = MenuItem()

is_on = True
profit = 0

while is_on:
    choice = input(f"What kind of coffee would you like? Type {menu.get_items()} ")
    
    if choice == 'report':
        coffee_maker.report()
        money_machine.report()
    elif choice == 'off':
        print("Machine is shutting down...")
        is_on = False
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)