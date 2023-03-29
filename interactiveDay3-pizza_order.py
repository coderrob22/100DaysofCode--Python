print("Welcome to the Papa Johns Ordering System!!!")

pizza_size = input("What size pizza would you like? S, M, or L? ")
pepperoni = input("Would you like pepperoni? ")
extra_cheese = input("Would you like extra cheese? ")

total = 0

if pizza_size == 'S':
    total += 15
    if pepperoni == 'Y':
        total += 2
    
elif pizza_size == 'M':
    total += 20
    if pepperoni == 'Y':
        total += 3
else:
    total += 25
    if pepperoni == 'Y':
        total += 3

if extra_cheese == 'Y':
    total += 1

print(f"Your final bill is: {total}.")