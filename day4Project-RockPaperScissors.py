import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
choice = int(input("Rock, paper, scissors says shoot!\nChoose 0 for rock, 1 for paper, or 2 for scissors.\n"))
their_pick= ''

opponent_selects = random.randint(0, 2)
if opponent_selects == 0:
    their_pick = rock
elif opponent_selects == 1:
    their_pick = paper
else:
    their_pick = scissors

if choice == 0 and their_pick == paper:
    print(f"You lose!\n The opponent chose paper...\n {rock}\nCan't beat\n{paper}")
elif choice == 0 and their_pick == scissors:
    print(f"You win!\n The computer chose scissor...\n {rock}\nSmashes!!!\n{scissors}")
elif choice == 0 and their_pick == rock:
    print(f"Tie, they chose rock too..\ngo again! \n {rock}\nTies\n{rock}")
elif choice == 1 and their_pick == scissors:
    print(f"You lose! \n {paper}\nCan't beat\n{scissors}")
elif choice == 1 and their_pick == rock:
    print(f"You win! \n {paper}\nCovers\n{rock}")
elif choice == 1 and their_pick == paper:
    print(f"Tie, go again! They chose paper too \n {paper}\nTies\n{paper}")
elif choice == 2 and their_pick == rock:
    print(f"You lose! \n {scissors}\nCan't beat\n{rock}")
elif choice == 2 and their_pick == paper:
    print(f"You win! \n {scissors}\nScissor cuts paper\n{paper}")
elif choice == 2 and their_pick == scissors:
    print(f"Tie, go again! \n {scissors}\nTies\n{scissors}")


