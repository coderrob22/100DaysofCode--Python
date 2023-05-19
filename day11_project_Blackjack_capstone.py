from blackjack_art import logo
import os
import random

#Logo setup and initial question setup. If you choose 'y' then the game will commence.
os.system("clear")
if input("Do you want to play blackjack? Please note: **This game DOES support the 5 Card Charlie.** \nType 'y' or 'no'. \n") == 'y':
    os.system("clear")
    print(logo)

    def play_again():
        # This is the setup for the cards, dealers hand, and your hand.
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        your_hand = []
        computer_hand = []
        game_over = False
        

    # This func will pick the randomized card.
        def deal():
            """ This is the function that will initially pick the randomized card."""
            card = random.choice(cards)
            return card
        
    # This function will calculate the total of the cards.
        def calculate_score(cards):
            """ This function will calculate the score of the cards in hand."""
            if sum(cards) == 21 and len(cards) == 2:
                return 0
            
            if sum(cards) > 21 and 11 in cards:
                cards.remove(11)
                cards.append(1)

            return sum(cards)
        
    # This function will compare the user's score with the computer's score.
        def compare(player_sum, computer_sum):
            if computer_sum == 0:
                return ("Blackjack! the computer wins!")
            elif player_sum < 21 and len(your_hand) == 5 and computer_sum < 21:
                return "WINNER 5 CARD CHARLIE!!! MuthaLuva!!!"   
            elif player_sum == 0:
                return("You win!!! Blackjack!!!")
            elif computer_sum > 21:
                return ("You win, the computer went over...")
            elif player_sum > 21:
                return ("You lose, you went over...")
            
            elif player_sum > computer_sum and player_sum < 22:
                return "You win, you had higher amount!!!"
            elif player_sum == computer_sum:
                return "Draw "   
            else: 
                return "You lost, mate..." 
            
            


    # This loop will pick 2 cards to give to the player.
        for _ in range(2):
            your_hand.append(deal())
            computer_hand.append(deal())

    # while loop to recheck everything everytime a new card is drawn.
        while not game_over:
        
        # Here is where the player and computer's score will be calculated.
            player_sum = calculate_score(your_hand)
            computer_sum = calculate_score(computer_hand)

        # Here is the print statement for showing cards    
            print(f"Your cards: {your_hand}. Your score is {player_sum}")
            print(f"Computer's first card: {computer_hand[0]} \n")

        # Game over logic has been added
            if player_sum == 0 or computer_sum == 0 or player_sum > 21:
                game_over = True
            else:
                if input("Would you like another card? Type 'y' or 'n'.\n") == 'y':
                    your_hand.append(deal())
                else:
                    game_over = True

        while computer_sum != 0 and computer_sum < 17:
            computer_hand.append(deal())
            computer_sum = calculate_score(computer_hand)

        print(f"    Your hand was {your_hand}, your final score was {player_sum}")
        print(f"    The computer's hand was {computer_hand} and score {computer_sum}")   
        print(compare(player_sum, computer_sum))
    os.system("clear")
    play_again()