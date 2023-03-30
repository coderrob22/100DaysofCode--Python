print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height > 120:
  print("You can ride the rollercoaster!!!")
  age = int(input("How old are you? "))
  if age < 12:
    print(f"You are only {age}, so you only pay $5.")
    bill += 5
  elif age < 18:
    print(f"You are {age}, so you get to pay $7 as a minor.")
    bill += 7
  elif age >= 45 and age <= 55:
    print("Your ticket is on the house since things are rough.")
  else:
    print(f"You are practically an adult, so you only pay $12.")
    bill += 12

  want_photo = input("Would you like your photo taken? Y or N? ")
  if want_photo == 'Y':
    bill += 3

  print(f"Your total amount is ${bill}")
    
else: 
  print("You are too short.")