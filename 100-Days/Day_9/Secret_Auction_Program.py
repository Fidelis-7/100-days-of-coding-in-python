import os


bids = {}
bidding_finished = False


def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"the winner is {winner} with the bid of ${highest_bid}")


while not bidding_finished:
    name = input("enter your name: ")      # ask bidder to input his/her name
    price = int(input("enter your bid price: $"))   # ask bidder to input his/herr bid price
    # Adding both the name and price into a dictionary
    bids[name] = price
    bidders = input("Are there any more bidders: type Yes or No: \n")   # check if there are more bidders
    if bidders == "no".lower():
        bidding_finished = True
        find_highest_bidder(bids)
    elif bidders == "yes".lower():
        os.system('cls')