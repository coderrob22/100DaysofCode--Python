import higher_lower_art
import higher_lower_data
import random
import os

# Show the logo
os.system('clear')
print(higher_lower_art.logo)

def check_answer(user_guess, num_follower_1, num_follower_2):
    """This takes the user's guess and compares it to the larger followers to see if the user guessed correctly"""
    if num_follower_1 > num_follower_2:
        return user_guess == 'a'
    else:
        return user_guess == 'b'

score = 0
proceed = True   
pick_2 = random.choice(higher_lower_data.data)

while proceed:

    ## Randomly select info from the API
    #Select A
    pick_1 = pick_2

    #Select B
    pick_2 = random.choice(higher_lower_data.data)

    while pick_1 == pick_2:
        pick_2 = random.choice(higher_lower_data.data)

    #Show info from A
    print(f"Compare A: {pick_1['name']}, a {pick_1['description']}, from {pick_1['country']}.\n")

    print(higher_lower_art.vs)

    #Show info from B
    print(f"Compare B: {pick_2['name']}, a {pick_2['description']}, from {pick_2['country']}.\n")


    # Ask the user to guess the answer
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        
    #Compare A and B and see which has more followers
    pick1_followers = pick_1['follower_count']
    pick2_followers = pick_2['follower_count']

    correct = check_answer(guess, pick1_followers, pick2_followers)

    #Adding the clear method and logo so that both are shown/done each go around the while loop.
    os.system('clear')
    print(higher_lower_art.logo)

    
    if correct:
        score += 1
        print(f"That was correct. Your score is {score}")
        

    else:
        print(f"Incorrect! Sorry, not sorry, game over. Your score was {score}")
        proceed = False
