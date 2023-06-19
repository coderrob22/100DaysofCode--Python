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


def make_coffee(drink_name, order_ingred):
    """Deduct the required ingredients from the resources"""
    for x in order_ingred:
        resources[x] -= order_ingred[x]
        print(f"Your {drink_name} has been served. Thank you. ENJOY!!! ☕️")

def enough_resources(orders_ingredients):
    """This func checks if the required resources to make the coffee product is available in the resources system"""
    for item in orders_ingredients:
        if orders_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def calculate_coin_amount(q, dime, nic, pennie):
    """This func returns calculated amount for coins inserted"""
    return .25 * q + dime * .10 + .05 * nic + .01 * pennie


def transaction_successful(total_money_inserted, cost_of_drink):
    """This func will check if you inserted enough money to buy the drink and return True if so, otherwise, False"""
    if total_money_inserted >= cost_of_drink:
        change = round(total_money_inserted - cost_of_drink, 2)
        print(f"Here is your change ${change}")
        global total_money
        total_money += cost_of_drink
        return True
    else:
        print("That's not enough money. Your money has been refunded to you")
        return False


turn_off = False
total_money = 0

while not turn_off:
    coffee_preference = input("What would you like? espresso/latte/cappuccino: ").lower()

    if coffee_preference == 'report':
        print(f"Water: {resources['water']}ml \nMilk: {resources['milk']}ml \nCoffee: {resources['coffee']}g \nMoney: ${total_money}")
    elif coffee_preference == 'off':
        turn_off = True
    else:
        drink = MENU[coffee_preference]
        if enough_resources(drink["ingredients"]):
            quarter = int(input("How many quarters are you inserting?"))
            dimes = int(input("How many dimes are you inserting?"))
            nickel = int(input("How many nickels are you inserting?"))
            penny = int(input("How many pennies are you inserting?"))
            your_payment = calculate_coin_amount(quarter, dimes, nickel, penny)
            if transaction_successful(your_payment, drink["cost"]):
                make_coffee(coffee_preference, drink["ingredients"])






# TODO: 1. Prompt user by asking "What would you like?"
# TODO: 2. Turn off the Coffee Machine by entering 'off' in the prompt
# TODO: 3. Print report
# TODO: 4. Check resource sufficiency
# TODO: 5. Process coins
# TODO: 6. Check if transaction successful
# TODO: 7. Make coffee
