import random


board = [' ' for _ in range(9)]


def print_board():
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")


def check_winner(player):
    wins = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for combo in wins:
        if all(board[i] == player for i in combo):
            return True
    return False


def get_empty_positions():
    return [i for i, v in enumerate(board) if v == ' ']



# COMPUTER AI LOGIC

def computer_move():
    empty = get_empty_positions()


    for move in empty:
        board[move] = 'O'
        if check_winner('O'):
            return
        board[move] = ' '


    for move in empty:
        board[move] = 'X'
        if check_winner('X'):
            board[move] = 'O'
            return
        board[move] = ' '


    move = random.choice(empty)
    board[move] = 'O'



# SINGLE PLAYER MODE

def single_player():
    moves = 0
    while True:
        print_board()


        try:
            move = int(input("Enter your move (1–9): ")) - 1
            if move < 0 or move > 8 or board[move] != ' ':
                print(" Invalid move. Try again.")
                continue
        except ValueError:
            print("Enter a valid number.")
            continue

        board[move] = 'X'
        moves += 1

        if check_winner('X'):
            print_board()
            print(" You win!")
            break

        if moves == 9:
            print_board()
            print(" It's a draw!")
            break

        print("Computer is thinking...")
        computer_move()
        moves += 1

        if check_winner('O'):
            print_board()
            print("Computer wins!")
            break


# -------------------------
# TWO PLAYER MODE
# -------------------------
def two_player():
    current = 'X'
    moves = 0

    while True:
        print_board()
        print(f"Player {current}'s turn.")

        try:
            move = int(input("Enter position (1–9): ")) - 1
            if move < 0 or move > 8 or board[move] != ' ':
                print("Invalid move! Try again.")
                continue
        except ValueError:
            print("Enter a valid number.")
            continue

        board[move] = current
        moves += 1

        if check_winner(current):
            print_board()
            print(f" Player {current} wins!")
            break

        if moves == 9:
            print_board()
            print("It's a draw!")
            break

        current = 'O' if current == 'X' else 'X'



# MAIN MENU

def main():
    print("🎮 TIC TAC TOE")
    print("1. Single Player (vs Computer)")
    print("2. Two Players")

    choice = input("Choose mode (1/2): ")

    if choice == "1":
        single_player()
    elif choice == "2":
        two_player()
    else:
        print("Invalid choice!")


main()
