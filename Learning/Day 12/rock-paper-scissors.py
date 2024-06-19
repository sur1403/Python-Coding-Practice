import random

def rock_paper():
    moves = ['rock', 'paper', 'scissors']
    while True:
        user_input = random.choice(moves)
        print(f"User chose: {user_input}")

        
        computer_move = random.choice(moves)
        print(f"Computer chose: {computer_move}")

        if user_input == computer_move:
            print("Its a Tie")
        
        elif computer_move == 'scissors' and user_input == 'paper' or computer_move == 'paper' and user_input == 'rock' or computer_move == 'rock' and user_input == 'paper':
            print("computer wins")
        elif computer_move == 'paper' and user_input == 'scissors' or computer_move == 'rock' and user_input == 'paper' or computer_move == 'scissors' and user_input == 'rock':
            print("User wins")
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again!='yes':
            print("Thanks for Playing")
            break
rock_paper()
      

