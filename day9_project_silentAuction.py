import os
from blind_auction_art import logo
print(logo)

call_again = True
bidding_dictionary = {}
winner = ""
def find_highest_bidder(bidding_rec):
    highest_bid = 0

    for x in bidding_rec:
        bid_amount = bidding_rec[x]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = x
    print(f"The winner is {winner}")

while call_again:
    name = input("What is your name? \n")
    bid = int(input("What's your bid? \n"))
    repeat = input("Is there another bidder? Type 'yes' or 'no' \n")
    bidding_dictionary[name] = bid
    if repeat == "no":
        call_again = False
        find_highest_bidder(bidding_dictionary)
    elif repeat == 'yes':
        os.system("clear")
