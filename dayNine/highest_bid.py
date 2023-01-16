from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.
print(logo)
print("Welcome to the secret auction program.")
bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record): 
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        if bidding_record[bidder] > highest_bid:
            highest_bid = bidding_record[bidder]
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}.")

while not bidding_finished:
  name = input("What is your name? ")
  bid = int(input("What's your bid? $"))
  bids[name] = bid

  should_continue = input("Are there any other bidders? Type 'yes' or 'no' ").lower()
  if should_continue == 'no':
    bidding_finished = True
  elif should_continue == 'yes':
    clear()
find_highest_bidder(bids)