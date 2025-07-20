import os
from art import logo
print(logo)

bid = {}
finish = False

def highest_bidding(bid_record):
    highest_bid = 0
    winner_name = ''
    for i in bid_record:
        if bid_record[i] > highest_bid:
            highest_bid = bid_record[i]
            winner = i
    print(f"The winner is {winner} with a bid of ${highest_bid}")
            
while not finish:
    name = input("Enter the name: ")
    bid_price = int(input("Enter the bidding amount: "))
    bid[name] = bid_price
    user = input("Any other users(Y/N): ")
    if user.lower() == 'n':
        finish = True
        highest_bidding(bid)
    else:
        os.system('cls')
        #finish = False /*If you don't want to clear screen use the condition "finish=False"*/

