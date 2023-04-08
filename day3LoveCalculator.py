# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

t = name1.lower().count('t')
r = name1.lower().count('r')
u = name1.lower().count('u')
e = name1.lower().count('e')

t2 = name2.lower().count('t')
r2 = name2.lower().count('r')
u2 = name2.lower().count('u')
e2 = name2.lower().count('e')

true_total = t + r + u + e + t2 + r2 + u2 + e2

l = name1.lower().count('l')
o = name1.lower().count('o')
v = name1.lower().count('v')
e3 = name1.lower().count('e')

l2 = name2.lower().count('l')
o2 = name2.lower().count('o')
v2 = name2.lower().count('v')
e4 = name2.lower().count('e')

love_total = l + o + v + e3 + l2 + o2 + v2 + e4

combined_score = str(true_total) + str(love_total)

if int(combined_score) < 10 or int(combined_score) > 90:
    print(f"Your score is {combined_score}, you go together like coke and mentos.")
elif int(combined_score) >= 40 and int(combined_score) <= 50:
    print(f"Your score is {combined_score}, you are alright together.")
else:
    print(f"Your score is {combined_score}.")