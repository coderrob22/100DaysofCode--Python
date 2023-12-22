names = {'Alex', 'Beth', 'Caroline', 'Dave', 'Eve', 'Freddie'}

import random

student_scores ={student:random.randint(1, 100) for student in names}

# passed_scores = {new_key:new_value for (key, value) in dictionary.items()}

passed_scores = {student:score for (student, score) in student_scores.items() if score >= 60}

###################################################

sentence = input()
# 🚨 Don't change code above 👆
# Write your code below 👇

list = sentence.split()
result = {word:len(word) for word in list}


print(result)