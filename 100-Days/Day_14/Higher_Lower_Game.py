# todos

from Game_data import data
from logo import higher_lower, vs
import random

# Display art
print(higher_lower)
score = 0
game_should_continue = True
account_B = random.choice(data)

def format_account(account):
    """Format the account data and returns the printable format."""
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_description}, from {account_country}"


def check_answer(guess, a_followers, b_followers):
    """take the user's guess and follower_counts and returns if they got it right."""

    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


# Make the game repeatable
while game_should_continue:
    # Generate a random account from the game data

    # Making account at position B become the next account at position A.
    account_A = account_B
    account_B = random.choice(data)
    while account_A == account_B:
        account_B = random.choice(data)

    print(f"Compare A: {format_account(account_A)}")
    print(vs)
    print(f"compare B: {format_account(account_B)}")

    # Ask user for a guess
    user_guess = input("who has more followers? type A or B: ").lower()

    # check if user is correct

    # Get follower count of each account
    follower_count_A = account_A["follower_count"]
    follower_count_B = account_B["follower_count"]

    is_correct = check_answer(user_guess, follower_count_A, follower_count_B)

    # Give user feedback on their guess
    # score keeping
    if is_correct:
        score += 1
        print(f"correct. your current score is {score}")
    else:
        game_should_continue = False
        print(f"sorry. that's wrong. score = {score}")


# clear the screen between rounds






