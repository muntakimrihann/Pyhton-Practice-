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
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    for combo in wins:
        if all(board[i] == player for i in combo):
            return True
    return False

def get_empty_positions():
    return [i for i, v in enumerate(board) if v == ' ']



# EASY MODE (Random Move)

def computer_easy():
    move = random.choice(get_empty_positions())
    board[move] = 'O'



# MEDIUM MODE (Win → Block → Random)

def computer_medium():
    empty = get_empty_positions()

    # 1. Try to Win
    for move in empty:
        board[move] = 'O'
        if check_winner('O'):
            return
        board[move] = ' '

    # 2. Try to Block Player
    for move in empty:
        board[move] = 'X'
        if check_winner('X'):
            board[move] = 'O'
            return
        board[move] = ' '

    # 3. Random Move
    computer_easy()



# HARD MODE (Unbeatable Minimax AI)

def minimax(is_maximizing):
    if check_winner('O'):
        return 1
    if check_winner('X'):
        return -1
    if ' ' not in board:
        return 0

    if is_maximizing:
        best_score = -999
        for i in get_empty_positions():
            board[i] = 'O'
            score = minimax(False)
            board[i] = ' '
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = 999
        for i in get_empty_positions():
            board[i] = 'X'
            score = minimax(True)
            board[i] = ' '
            best_score = min(score, best_score)
        return best_score


def computer_hard():
    best_score = -999
    best_move = None

    for i in get_empty_positions():
        board[i] = 'O'
        score = minimax(False)
        board[i] = ' '
        if score > best_score:
            best_score = score
            best_move = i

    board[best_move] = 'O'



# SINGLE PLAYER WITH DIFFICULTY

def single_player(difficulty):
    moves = 0

    while True:
        print_board()

        # Player move
        try:
            move = int(input("Enter your move (1–9): ")) - 1
            if move < 0 or move > 8 or board[move] != ' ':
                print("❌ Invalid move. Try again.")
                continue
        except ValueError:
            print("Enter a number.")
            continue

        board[move] = 'X'
        moves += 1

        if check_winner('X'):
            print_board()
            print("🎉 You win!")
            break

        if moves == 9:
            print_board()
            print("🤝 Draw!")
            break

        # COMPUTER MOVE
        print("🤖 Computer is thinking...\n")

        if difficulty == "easy":
            computer_easy()
        elif difficulty == "medium":
            computer_medium()
        else:
            computer_hard()

        moves += 1

        if check_winner('O'):
            print_board()
            print("💀 Computer wins!")
            break




# MAIN MENU

def main():
    print("\n🎮 TIC TAC TOE — Difficulty Mode\n")
    print("Choose difficulty:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard (Unbeatable)")

    choice = input("Enter 1, 2, or 3: ")

    if choice == "1":
        single_player("easy")
    elif choice == "2":
        single_player("medium")
    elif choice == "3":
        single_player("hard")
    else:
        print("Invalid option!")


main()
