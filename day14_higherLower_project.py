import higher_lower_art
import higher_lower_data
import random

# Show the logo
print(higher_lower_art.logo)


## Randomly select info from the API
#Select A
pick_1 = random.choice(higher_lower_data.data)

#Select B
pick_2 = random.choice(higher_lower_data.data)

if pick_1 == pick_2:
    pick_2 = random.choice(higher_lower_data.data)

score = 0


    

#Show info from A
print(f"Compare A: {pick_1['name']}, a {pick_1['description']}, from {pick_1['country']}.\n")

print(higher_lower_art.vs)

#Show info from B
print(f"Compare B: {pick_2['name']}, a {pick_2['description']}, from {pick_2['country']}.\n")

if input("Who has more followers? Type 'A' or 'B': ") == answer:
    score += 1
else: 
    print("Sorry that is incorrect. Game Over")
    GameOver





#Compare A and B and see which has more followers
#Receive input
#Compare the input to the answer... if the input and answer are the same...increment score...if not, game over