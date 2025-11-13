
def reset_board():
    return [' ' for _ in range(9)]
def print_board(board):
    print("\nCurrent Board:")
    print(f" {board[0]} | {board[1]} | {board[2]}     1 | 2 | 3")
    print("---+---+---   ---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]}     4 | 5 | 6")
    print("---+---+---   ---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]}     7 | 8 | 9\n")


def check_winner(board, player):
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
    print("🎮 Welcome to Tic Tac Toe!")
    p1 = input("Enter Player 1 name (X): ")
    p2 = input("Enter Player 2 name (O): ")

    scores = {p1: 0, p2: 0, "Draws": 0}

    while True:
        board = reset_board()
        current = 'X'
        moves = 0

        while True:
            print_board(board)
            player_name = p1 if current == 'X' else p2
            print(f"{player_name}'s turn ({current})")

            try:
                move = int(input("Choose position (1–9): ")) - 1
                if move < 0 or move > 8 or board[move] != ' ':
                    print("❌ Invalid move. Try again.")
                    continue
            except ValueError:
                print("Please enter a valid number.")
                continue

            board[move] = current
            moves += 1


            if check_winner(board, current):
                print_board(board)
                print(f"🎉 {player_name} wins this round!")
                scores[player_name] += 1
                break


            if moves == 9:
                print_board(board)
                print("🤝 It's a draw!")
                scores["Draws"] += 1
                break

            current = 'O' if current == 'X' else 'X'


        print("\n🏆 Scoreboard:")
        for k, v in scores.items():
            print(f"{k}: {v}")


        again = input("\nPlay another round? (y/n): ").lower()
        if again != 'y':
            print("\nThanks for playing! Final Scores:")
            for k, v in scores.items():
                print(f"{k}: {v}")
            print("Goodbye 👋")
            break


play_game()
