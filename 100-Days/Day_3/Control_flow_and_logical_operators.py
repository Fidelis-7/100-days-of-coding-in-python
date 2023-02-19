# checking for odd or even numbers

# number = int(input("enter a number: "))
# if number % 2 == 0:
#     print(f"{number} is an even number")
# else:
#     print(f"{number} is an odd number")


# checking for the height and age of persons to ride a roller coaster and to see if the want to take photos
# height = float(input("enter your height: "))
# if height >= 120:
#     print("you can ride")
#     age = int(input("enter your age: "))
#     if age < 12:
#         bill = 5
#         print("your bill is $5")
#     elif age <= 18:
#         bill = 7
#         print("your bill is 7")
#     else:
#         bill = 12
#         print("your bill is $12")
#     take_photo = input("Do you want to take a photo? ")
#     if take_photo == "yes":
#         bill += 3
#         print(f"your total bill is ${bill}")
#     else:
#         print(f"your total bill is ${bill}")
#
# else:
#     print("you cant ride")



# updated BMI calculator

# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))
# bmi = weight / (height ** 2)
# print(round(bmi, 2))
# if bmi < 18.5:
#     print(f"your bmi is {bmi}, you are underweight")
# elif bmi < 25:
#     print(f"your bmi is {bmi}, you have normal weight")
# elif bmi < 30:
#     print(f"your bmi is {bmi}, you are overweight")
# elif bmi < 35:
#     print(f"your bmi is {bmi}, you are obese")
# else:
#     print(f"your bmi is {bmi}, clinically you are obese")


# calculating for leap years

# year = int(input("what year do you want to check: "))
# if year % 4 == 0:
#     print("leap year")
#     if year % 100 == 0:
#         print("a leap year")
#     elif year % 400 == 0:
#         print("leap year")
# else:
#     print(f"{year} is not a leap year")


# pizza order challenge
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size do you want? S, M, or L? ")
# add_pepperoni = input("Do you want pepperoni? Y or N? ")
# extra_cheese = input("Do you want extra cheese? Y or N? ")
#
# # prices of pizza
# small_pizza = 15
# medium_pizza = 20
# large_pizza = 25
#
# pepperoni_for_small_pizza = 2
# pepperoni_for_medium_or_large_pizza = 3
# extra_cheese_for_any_size_pizza = 1
#
# # condition
# bill = 0
# if size == "s".lower():
#     bill += 15
# elif size == "m".lower():
#     bill += 20
# elif size == "l".lower():
#     bill += 25
# else:
#     print("invalid command")
#
# if add_pepperoni == "y".lower():
#     if size == "s".lower():
#         bill += 2
#     elif size == "m".lower() or size == "l".lower():
#         bill += 3
# else:
#     pass
#
# if extra_cheese == "y".lower():
#     bill += 1
# print(f"your final bill is {bill}")


# Love calculator challenge
# print("Welcome to the love calculator challenge")
# boy_name = input("Enter boy's name: ")
# girl_name = input("Enter girl's name: ")
# word1 = "True"
# word2 = "Love"
# full_name = boy_name + " " + girl_name
# total_word = word1 + " " + word2
# lowercase_fullname = full_name.lower()
# lowercase_total_word = total_word.lower()
#
# t = lowercase_fullname.count("t")
# r = lowercase_fullname.count("r")
# u = lowercase_fullname.count("u")
# e = lowercase_fullname.count("e")
#
# l = lowercase_fullname.count("l")
# o = lowercase_fullname.count("o")
# v = lowercase_fullname.count("v")
# i = lowercase_fullname.count("e")
#
# true = t + r + u + e
# love = l + o + v + i
# loveScore = int(str(true) + str(love))
# if loveScore < 10 or loveScore > 90:
#     print(f"your lovescore is {loveScore}. You guys go like coke and mint")
# elif loveScore >= 40 and loveScore <= 50:
#     print(f"your lovescore is {loveScore}. you go alright together")
# else:
#     print(f"your lovescore is {loveScore}")


# Treasure island challenge

# print("Welcome to treasure island")
# print("your mission is to find the treasure")
# game_over = False
# choice_of_direction = input("Please choose left or right: ")
# if choice_of_direction == "right".lower():
#     print("You lose")
#     game_over = True
# elif choice_of_direction == "left".lower():
#     next_move = input("you have reached an ocean. do you wish to swim through or wait for a boat? ")
#     if next_move == "swim".lower():
#         print("you lose.. a shark bit you")
#         game_over = True
#     else:
#         print("i will wait for a boat")
#         next_choice = input("you have arrived safely. Now pick a door to open: red, blue, or yellow: ")
#         if next_choice == "red".lower():
#             print("you lose")
#             game_over = True
#         elif next_choice == "blue".lower():
#             print("you lose")
#             game_over = True
#         else:
#             print("yay you win")