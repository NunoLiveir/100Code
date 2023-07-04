print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Pandi and Ginja's Escape Room.")
print("Your mission is to find the treasure.") 


step_one = input("You arrive home! You hear faint sounds of meowing and that already tells you, you are in danger! Quick! Do you turn left, or do you turn right? Type left or right: ")

if step_one == "left":
  step_two = input("Phew! You managed to escape the monster! However, you are not out of harm's way yet. You hear meowing again! However, a different one this time! Do you wait it out, or keep moving? Type wait or move: ")
  if step_two == "move":
    step_three = input("Another great decision! Your mission is almost complete. OH no! Three, closed doors now stand in your way! Only behind one of them can you find the treasure! Type yellow, blue or red: ")
    if step_three == "yellow":
      print("Victory! You win! You have found the almighty treasure!!!")
    elif step_three == "blue":
      print("Oh no! You enter a room full of wet, cat food! The beasts draw near and there is no escape. You lose!")
    elif step_three == "red":
      print("The door is old and creaky which raises the beasts' attention! Both come running and soon enough you are jumped by them! You lose!")
    else:
      print("Game over! Read the prompt!!")
  else:
    print("That was not a wise choice! As you patiently wait around, one of the beasts turns around the corner and comes running at you! You lose.")
else:
  print("Your run is cut short because Pandora is there, and she is HUNGRY!! You lose!")
