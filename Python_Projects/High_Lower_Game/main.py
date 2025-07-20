from game_data import data
import random
from art import logo, vs
import os

#For getting the data
def get_data():
    return random.choice(data)

#For printing the details in format
def account_details(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"

#For the highest number of followers
def check_answer(guess, a, b):
    a_followers = a["follower_count"]
    b_followers = b["follower_count"]
    print(f"a_followers: {a_followers}, b_followers: {b_followers}")
    if a_followers > b_followers:
        return guess == 'a'     #Gives boolean value
    else:
        return guess == 'b'     #Gives boolean value

def game():
    print(logo)
    score = 0
    profile_a = get_data()
    profile_b = get_data()
    #print(profile_a, profile_b, sep='\n')
    game_over = False
    while not game_over:  
        profile_a = profile_b
        profile_b = get_data()
        if profile_a == profile_b:
            profile_b = get_data()
        print(f"Compare A: {account_details(profile_a)}.")
        print(vs)
        print(f"Against B: {account_details(profile_b)}.")
            
        user_guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        
        answer = check_answer(user_guess, profile_a, profile_b)
        os.system('clear')
        print(logo)
        if answer:
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            game_over = True    
game()