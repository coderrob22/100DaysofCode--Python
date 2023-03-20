print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
percent = int(input("What percentage tip would you like to give? 10, 12, 15, or 18? "))
split = int(input("How many people to split the bill? "))

tip_percent = percent / 100
tip_amount = tip_percent * bill

cumulative_total_with_tip = bill + tip_amount

total = cumulative_total_with_tip / split
total_rounded_2decimals = "{:.2f}".format(total)

print(f"Each person should pay: ${total_rounded_2decimals}")