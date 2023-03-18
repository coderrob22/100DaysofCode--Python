age = input("How old are you? ")

months = (90 * 12)- (int(age)*12)
weeks = (90 * 52)- (int(age)*52)
days = (90 * 365)- (int(age)*365)

print(f"You have {days} days, {weeks} weeks, and {months} months left.")