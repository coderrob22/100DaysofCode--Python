import higher_lower_art
import higher_lower_data
import random

# Show the logo
print(higher_lower_art.logo)

# Randomly select info from the API
pick_1 = higher_lower_data.data[random.randint(0, len(higher_lower_data.data))]
pick_2 = higher_lower_data.data[random.randint(0, len(higher_lower_data.data))]

print(f"Compare A: {pick_1['name']}, a {pick_1['description']}, from {pick_1['country']}.\n")

print(higher_lower_art.vs)

print(f"Compare B: {pick_2['name']}, a {pick_2['description']}, from {pick_2['country']}.\n")
