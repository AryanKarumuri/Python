from art import logo
print(logo)


MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = {
    "value": 0,
}



#To display the details of resources
def display_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money['value']}")


#To check whether the resources are sufficient or not
def check_coffee_resources(user_coffee_choice):
    for item in MENU[user_coffee_choice]['ingredients']:
        if MENU[user_coffee_choice]['ingredients'][item] > resources[item]:
            print(f"​Sorry there is not enough {item}.")
            return False
    return True
    

#To the know total amount given by a user
def process_coins():
    print("Insert the coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


#Checking whether the transaction is possible or not
def check_transaction_status(user_coffee_choice, coffee_cost):
    if coffee_cost >= MENU[user_coffee_choice]['cost']:
        change = round(coffee_cost - MENU[user_coffee_choice]['cost'], 2)
        print(f"Here's your change {change}")
        money['value'] += MENU[user_coffee_choice]['cost']
        return True
    else:
        print(f"Sorry that's not enough money. Money refunded {coffee_cost}.")
        return False
    

def make_coffee(user_coffee_choice):
    for item in MENU[user_coffee_choice]['ingredients']:
        resources[item] -= MENU[user_coffee_choice]['ingredients'][item]
    print(f"Here is your {user_coffee_choice} ☕️. Enjoy!")
    
def coffee():
    is_on = True
    while is_on:
        user_choice = input("​What would you like? (espresso/latte/cappuccino):").lower()
        if user_choice == "off":
            is_on = False
        elif user_choice == "report":
            display_report()
            coffee()
        elif check_coffee_resources(user_choice):
            total_amount = process_coins()
            if check_transaction_status(user_choice, total_amount):
                make_coffee(user_choice)
            
coffee()       
        
    

