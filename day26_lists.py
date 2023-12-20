numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above 👆

# Write your 1 line code 👇 below:
squared_numbers = [x * x for x in numbers]
# Write your code 👆 above:


print(squared_numbers)

###################################################

list_of_strings = input().split(',')
# 🚨 Do  not change the code above

# TODO: Use list comprehension to convert the strings to integers 👇:
result = [int(x) for x in list_of_strings if int(x) % 2 == 0]

# TODO: Use list comprehension to filter out the odd numbers
# and store the even numbers in a list called "result"


# Write your code 👆 above:
print(result)

################################################################

with open('file1.txt') as f1:
  first_file = f1.readlines()

with open('file2.txt') as f2:
  second_file =f2.readlines()

result = [int(x) for x in first_file if x in second_file]


# Write your code above 👆
print(result)