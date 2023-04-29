import random
#  10 represents jack, king and Queen
# 11 represents Ace

restart = True
# create a deal_Card function that uses the list below to return a random card
def deal_card():
    '''returns a random card from deck'''
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


# create a function called calculate_score() that takes a list of cards as input
# and returns the score
# look up the  sum() function to help you do this
def calculate_score(cards):
    """Take a list of cards and return the score calculated from the card"""
    # inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10)
    # and return 0 instead of the actual score. 0 will represent blackjack in our game.
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    # inside calculate_score() check for an 11(ace). if the score is already over 21,
    # remove the 11 and replace it with a 1. you might need to look up append() and remove().
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


# create a function called compare() and pass in the user_score and computer_score. if
# the computer and user both have the same score, then it's a draw. if the computer has a blackjack(0),
# then the user losses. if the user has a blackjack(0), then the user wins. if the user_score is over 21,
# the user loses. if the computer_score is over 21, then the computer loses. if none of the above, then the
# player with the highest score wins.
def compare(user_score, computer_score):
    if user_score == computer_score:
        return "it's a draw"
    elif computer_score == 0:
        return "computer wins"
    elif user_score == 0:
        return "User wins"
    elif user_score > 21:
        return "user lost. you exceeded"
    elif computer_score > 21:
        return "computer lost. you exceeded"
    elif user_score > computer_score:
        return "user wins"
    else:
        return "computer wins"


def play_again():
    # Deal the user and computer 2 cards each using deal_card()
    user_cards = []
    computer_cards = []
    is_game_over = False
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        # call calculate_score(). if the computer or the user has a blackjack (0) or if the
        # user's score is over 21, then the game ends.
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}") # to display the user's cards
        print(f"Computer's first card: {computer_cards[0]}")  # to display the dealer's first card
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
    # if the game has not ended, ask the user if they want to draw another card. if yes,
    # then use the deal_card() function to add another card to the user_cards List. if no,
    # then the game has ended
        else:
            draw_another_card = input("Do you want to draw another card? type 'yes' or 'no': ")
            if draw_another_card == "yes".lower():
                user_cards.append(deal_card())
            else:
                is_game_over = True

    # once the user is done, it's time to let the computer play. The computer should keep drawing cards
    # as long as it has a score less than 17.
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"your final hand: {user_cards}, final_score: {user_score}")
    print(f"computer's final hand: {computer_cards}, final score:{computer_score}")
    print(compare(user_score, computer_score))


# to restart the game
while input("Do you want to play a game of BlackJack? type 'yes' or 'no': ") == 'yes':
    print(play_again())
else:
    restart = False


   

