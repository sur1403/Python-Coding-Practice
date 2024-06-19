import random
from words import words

word = "secret"
allowed_error = 7
guesses = []
done = False

while not done:
    for letter in word:
        if letter.lower() in guesses:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print("")

    guess = input(f"Allowed input errors {allowed_error}, Next Guess: ")
    guesses.append(guess.lower())
    if guess.lower() not in word.lower():
        allowed_error -= 1
        if allowed_error == 0:
           break
    done = True
    for letter in word:
        if letter.lower() not in guesses:
            done =  False

if done:
    print(f"You found the word. It was {word}")  
else: 
    print("Game over. This was {word}")         









