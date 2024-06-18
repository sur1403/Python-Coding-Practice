instructions = """"
This will be our tic tac board


1 | 2 | 3
---------
4 | 5 | 6
---------
7 | 8 | 9

"""

sign_dictionary = []
for i in range(9):
    sign_dictionary.append(' ')
print("sign", sign_dictionary)

def print_board():
    board = f"""
        {sign_dictionary[0]} | {sign_dictionary[1]} | {sign_dictionary[2]}
        ---------
        {sign_dictionary[3]} | {sign_dictionary[4]} | {sign_dictionary[5]}
        ---------
        {sign_dictionary[6]} | {sign_dictionary[7]} | {sign_dictionary[8]}
    """
    print(board)

index_list = []
def take_input(playername):
    while True:
        x = int(input(f"{playername}: "))-1
        if 0 <= x < 10:
            if x in index_list:
                print("This spot is blocked")
                continue
            index_list.append(x)
            return x
        print("Please enter number between 1-9")


def calculate_result(player1, player2):
    if sign_dictionary[0] == sign_dictionary[1] == sign_dictionary[2] == 'X' or sign_dictionary[1] == sign_dictionary[4] == sign_dictionary[7] == 'X' or sign_dictionary[0] == sign_dictionary[3] == sign_dictionary[6] == 'X' or  sign_dictionary[2] == sign_dictionary[5] == sign_dictionary[8] == 'X' or sign_dictionary[3] == sign_dictionary[4] == sign_dictionary[5] == 'X' or sign_dictionary[2] == sign_dictionary[4] == sign_dictionary[6] == 'X' or sign_dictionary[6] == sign_dictionary[7] == sign_dictionary[8] == 'X' or sign_dictionary[0] == sign_dictionary[4] == sign_dictionary[8] == 'X' :
     print(f"Congratulations {player1} . !!! You Won")
     quit("Thanks you")
    
    elif sign_dictionary[0] == sign_dictionary[1] == sign_dictionary[2] == '0' or sign_dictionary[1] == sign_dictionary[4] == sign_dictionary[7] == '0' or sign_dictionary[0] == sign_dictionary[3] == sign_dictionary[6] == '0' or sign_dictionary[2] == sign_dictionary[5] == sign_dictionary[8] == '0' or sign_dictionary[3] == sign_dictionary[4] == sign_dictionary[5] == '0' or sign_dictionary[2] == sign_dictionary[4] == sign_dictionary[6] == '0' or sign_dictionary[6] == sign_dictionary[7] == sign_dictionary[8] == '0' or sign_dictionary[0] == sign_dictionary[4] == sign_dictionary[8] == '0' :
     print(f"Congratulations {player2} . !!! You Won")
     quit("Thanks you")
     

def main():
    print("Welocme to Tic tac Toe")
    player_1 = input("Enter name of Player1: ")
    player_2 = input("Enter name of Player2: ")
    print(f"Thank you for joining {player_1} and {player_2}")
    print(instructions)
    print(f"{player_1} is assigned with sign X")
    print(f"{player_2} is assigned with sign 0")
    input("Enter any key to star tthe game")

    print_board()

    for i in range(9):
        if i % 2 == 0:
            index = take_input(player_1)
            sign_dictionary[index] = 'X'
        else:
            index = take_input(player_2)
            sign_dictionary[index] = '0'
        print_board()

        calculate_result(player_1, player_2)


main()