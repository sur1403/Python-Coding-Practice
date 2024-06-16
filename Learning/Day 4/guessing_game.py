import random

def gussing_game():
    computer_number = random.randint(1, 100)
    print(computer_number)
    guess = None
    num_guesses = 0
    while guess != computer_number:
        guess = int(input("Enter any number"))
        num_guesses+=1
        if guess < computer_number:
            print("Too low")
        elif guess > computer_number:
            print("Too low")
        elif guess == computer_number:
            print("Bingo")
            break
    print(guess, num_guesses)
   
gussing_game()

