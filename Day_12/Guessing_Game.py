# welcome message
import random
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
difficulty_level = input("choose a difficulty: type 'easy' or 'hard': ")
# to get the random number between 1 and 100
random_number = random.randint(1, 100)
computer_choice = random_number
print(computer_choice)
lives = ""


# lives and attempts check
def attempts_and_lives_check():
    global lives
    for attempt in range(lives + 1):
        user_guess = int(input("Make a guess: "))
        lives -= 1
        if 10 > lives != 0:
            if user_guess != computer_choice:
                if user_guess > computer_choice:
                    print("too high")
                else:
                    print("too low")
                print(f"try again. you have {lives} lives left")
            elif user_guess == computer_choice:
                print("you are correct")
                break
        else:
            print("all lives used")
            break


# to check the difficulty level
if difficulty_level == "easy".lower():
    lives = 10
    print("you have 10 lives remaining to guess the number.")
    attempts_and_lives_check()


else:
    lives = 5
    print("you have 5 lives remaining to get the number.")
    attempts_and_lives_check()
