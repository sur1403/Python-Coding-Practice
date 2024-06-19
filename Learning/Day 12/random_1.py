import random

def guess(x):
    random_number = random.randint(1,100)
    print(random_number)
    chances = 0
    guess = 0
    while guess!=random_number:
        guess = int(input(f"Guess a number between 1 and  {x}:"))
        chances+=1
        if guess < random_number:
            print("Sorry, guess again, Too low")
        elif guess > random_number:
            print("Sorry, guess again, Too High")
        else:
            break
    print(f"You got the number right {random_number} in {chances} chances")

guess(100)