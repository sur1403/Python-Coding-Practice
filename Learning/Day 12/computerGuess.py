import random

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low<=high:
          guess = random.randint(low, high)
        else:
            print("Error: the range is invalid.")
            break
        feedback = input(f"Is {guess} to high(h), too low(l) or correct(c)!!").lower()
        if feedback == 'h':
                high = guess -1
        elif feedback == 'l':
                low = guess + 1
        elif feedback == 'c':
                print(f"Yayyy computer guessed your number {guess} correctly")
        else:
            print("Invalid input! Please enter 'h', 'l', or 'c'.")

computer_guess(10)


