import os
from art import logo

#Addition
def add(m, n):
    return m+n
    
#Subtraction
def sub(m, n):
    return m-n
    
#Multiplication
def mul(m, n):
    return m*n
    
#Division
def div(m, n):
    return m/n
    
#Exponential
def exp(m, n):
    return m**n

#Dictionary
operator_symbol = {
    "+" : add,
    "-" : sub,
    "*" : mul,
    "/" : div,
    "**": exp }

def calculate():
    print(logo)
    num1 = float(input("Enter the number: "))
    for i in operator_symbol:
        print(i)
    should_proceed = True 
    while should_proceed:
        selected_operator = input("Enter one operation from the above: ")
        calculate_function = operator_symbol[selected_operator]
        num2 = float(input("Enter the number: "))
        answer = calculate_function(num1, num2)
        print(f"{num1} {selected_operator} {num2} = {answer}")
        ask = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")
        if ask == 'y':
            num1 = answer
            continue
        else:
            should_proceed = False
            os.system('cls')
            calculate()
calculate()
    
    
    
    
    
    