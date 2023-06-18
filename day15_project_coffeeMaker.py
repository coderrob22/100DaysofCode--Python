MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

turn_off = False
total_money = 0

while not turn_off:
    coffee_preference = input("What would you like? espresso/latte/cappuccino: ").lower()

    if coffee_preference == 'report':
        print(f"Water: {resources['water']}ml \nMilk: {resources['milk']}ml \nCoffee: {resources['coffee']}g \nMoney: ${total_money}")
    elif coffee_preference == 'off':
        turn_off = True
    elif coffee_preference == 'espresso':
        if resources["water"] >= MENU["espresso"]["ingredients"]["water"] and resources["coffee"] >= MENU["espresso"]["ingredients"]["coffee"]:
            print('Please insert coins.')





# TODO: 1. Prompt user by asking "What would you like?"
# TODO: 2. Turn off the Coffee Machine by entering 'off' in the prompt
# TODO: 3. Print report
# TODO: 4. Check resource sufficiency
# TODO: 5. Process coins
# TODO: 6. Check if transaction successful
# TODO: 7. Make coffee