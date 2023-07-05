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



print("Welcome to the ever so serious and competitive game of RPS: Rock, Paper, Scissors!")
choice = input("Choose your weapon! To choose rock type '0', for paper type '1' and for scissors type '2': ")
fchoice = int(choice)


if fchoice == 0:
  print(rock)
elif fchoice == 1:
  print(paper)
else:
  print(scissors)

print("The computer chose: ")
comp_choice = random.randint(0,2)

if comp_choice == 0:
  print(rock)
elif comp_choice == 1:
  print(paper)
else:
  print(scissors)

if fchoice == comp_choice:
  print("It's a tie!")

if fchoice == 0 and comp_choice == 2:
  print("Victory! Humanity wins!")
elif fchoice == 0 and comp_choice == 1:
  print("Defeat! I, for once, welcome our computer overlords.")
  
if fchoice == 1 and comp_choice == 2:
  print("Defeat! I, for once, welcome our computer overlords.")
elif fchoice == 1 and comp_choice == 0:
  print("Victory! Humanity wins!")

if fchoice == 2 and comp_choice == 0:
  print("Defeat! I, for once, welcome our computer overlords.")
elif fchoice == 2 and comp_choice == 1:
  print("Victory! Humanity wins!")
  
