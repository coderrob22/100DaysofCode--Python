import name_that_number_art
import random

print(name_that_number_art.logo)

print("Welcome to Name that Number!!!")
print("I am thinking of a number between 1 and 100. Can you guess it? Let's see...")

what_difficulty = input("What difficulty would you like? Type 'easy' or 'hard':\n")

if what_difficulty == 'easy':
    tries = 10
elif what_difficulty == 'hard':
    tries = 5

name_that_number = random.randint(1, 101)


while tries > 0:
    guess = int(input(f"What number do you think I am guessing? You have {tries} tries.\n"))
    if guess > name_that_number:
        print(f"Too high.. \n")
        tries -= 1
        
    elif guess < name_that_number:
        print("too low\n")
        tries -= 1
        
    else:
        print("You got it, you win!!!\n")
        tries = 0

    if tries == 0 and guess != name_that_number:
        print("You ran out of guess...You lose. \n")