user_input = input("Please enter all the score so we can calulate the highest one\n")
score_list = user_input.split()

#This is to make sure all the numbers being entered are integers
for x in range(0, len(score_list)):
    score_list[x] = int(score_list[x])

#This will be the main loop to print the numbers
highest_score = 0
for score in score_list:
    if score > highest_score:
        highest_score = score
print(f"The highest score is: {highest_score}")
