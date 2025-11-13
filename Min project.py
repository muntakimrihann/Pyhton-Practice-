# 🎮 Tic Tac Toe Game (2 Players)

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
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    for combo in wins:
        if all(board[i] == player for i in combo):
            return True
    return False


def play_game():
    current = 'X'
    moves = 0

    while True:
        print_board()
        print(f"Player {current}'s turn.")
        try:
            move = int(input("Enter position (1–9): ")) - 1
            if move < 0 or move > 8 or board[move] != ' ':
                print(" Invalid move. Try again.")
                continue
        except ValueError:
            print("Please enter a valid number.")
            continue

        board[move] = current
        moves += 1


        if check_winner(current):
            print_board()
            print(f"🎉 Player {current} wins!")
            break


        if moves == 9:
            print_board()
            print("🤝 It's a draw!")
            break

        # Switch player
        current = 'O' if current == 'X' else 'X'

play_game()
