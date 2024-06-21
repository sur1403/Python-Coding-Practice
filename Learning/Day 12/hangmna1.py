import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)  # Choose a random word from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)  # Ensure the word doesn't contain '-' or ' '
    return word.upper()  # Convert the word to uppercase for consistency

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # Set of letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # Set of letters guessed by the user

    lives = 6
    while len(word_letters) > 0 and lives > 0:
        # Show the user which letters have been guessed and the current state of the word
        print("Letters used: ", ' '.join(used_letters))
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        # Get user input for a letter
        user_letter = input("Guess a letter: ").upper()

        if user_letter in alphabet - used_letters:  # Check if the input is a valid letter
            used_letters.add(user_letter)  # Add the letter to the used letters set

            if user_letter in word_letters:
                word_letters.remove(user_letter)  # Remove the guessed letter from the word letters set
            else: 
                lives -= 1
                print("Letter is not in word")

        elif user_letter in used_letters:
            print("You have already guessed that letter. Please try again.")

        else:
            print("Invalid character. Please try again.")

    # When len(word_letters) == 0, the loop exits because all letters have been guessed
    print(f"Congratulations! You guessed the word '{word}' correctly.")

hangman()
