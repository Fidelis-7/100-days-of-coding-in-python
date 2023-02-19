# fruits = ["apple", "mango"]
# fruits.append("banana")
# fruits.extend(["cherry", "orange", "lemon"])
# fruits[2] = "strawberry"
# print(fruits)


# Banker roulette challenge
# import random
# names_string = input("Give me everybody's names, seperated by a comma. ")
# names = names_string.split(", ")
# pay_bill = random.choice(names)
# print(pay_bill)
# print(f"{pay_bill} is going to pay the bill")


# Treasure Map challenge
# row_1 = [" ", " ", " "]
# row_2 = [" ", " ", " "]
# row_3 = [" ", " ", " "]
# map = [row_1, row_2, row_3]
# print(f"{row_1}\n{row_2}\n{row_3}")
# position = input("where do you want to put the treasure? ")
#
# horizontal = int(position[0])
# vertical = int(position[1])
#
# selected_row = map[vertical - 1]
# selected_row[horizontal - 1] = "X"
#
#
# print(f"{row_1}\n{row_2}\n{row_3}")



# Rock paper scissors challenge

import random
rock = 0
paper = 1
scissors = 2
objects = [rock, paper, scissors]
player_choice = int(input("which object will you pick? "))
computer_choice = random.choice(objects)

if player_choice == 0 and computer_choice == 2:
    print(f"player chose rock, computer chose scissors")
    print("player wins")
elif player_choice == 2 and computer_choice == 1:
    print(f"player chose scissors, computer chose paper")
    print("player wins")
elif player_choice == 1 and computer_choice == 0:
    print(f"player chose paper, computer chose rock")
    print("player wins")
else:
    print(f"player chose {player_choice}, computer chose {computer_choice}")
    print("computer wins")
