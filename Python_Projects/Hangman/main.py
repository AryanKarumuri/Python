import random

form hangman_words import words_list

number_of_lives = 6
end_of_game = False
selected_word = random.choice(words_list)
print(f"The selected word is {selected_word}")

from hangman_lives_art import logo
print(logo)

display_word = []

for _ in range(len(selected_word)):
    display_word += "_"
    
while not end_of_game:
    guess = input("Guess a letter: ").lower()
        
    for position in range(len(selected_word)):
        if guess == selected_word[position]:
            print(f"You've already guessed {guess}")
            display_word[position] = guess
        
    if guess not in selected_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        number_of_lives -= 1
        if number_of_lives == 0:
            end_of_game = True
            print("You lose.")
        
    print(f"{' '.join(display_word)}")

    if "_" not in display_word:
        end_of_game = True
        print("You win.")
    
    from hangman_lives_art import stages
    print(stages[number_of_lives])
    
    
    
    
    