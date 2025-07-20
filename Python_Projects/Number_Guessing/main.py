import random

print("---->Welcome to Number Guessing Game!<----")
print("I'm thinking of a number in between 1 to 100. Can you guess it?")
correct_answer = random.randint(1, 100)
#For knowing the selected number
print(f"Correct answer is: {correct_answer}")

def difficulty():
    difficulty_level = input("Choose the difficulty easy or hard: ")
    if difficulty_level == "easy":
        return 10
    elif difficulty_level == "hard":
        return 5

def game():
    chances = difficulty()
    if isinstance(chances, int):
        while chances > 0:
            print(f"You have {chances} attempts remaining to guess the number")
            guessed_number = int(input("Make a guess: "))
            if guessed_number == correct_answer:
                print("Hurray!!!You guessed the number")
                break
            elif guessed_number > correct_answer:
                print("Guessed number is too high")
            else:
                print("Guessed number is too low")
            chances -= 1
        if chances == 0 and guessed_number != correct_answer:
            print("Oops!!! You've ran out of guesses, you lose")
    else:
        print("Please enter correct option")
game()