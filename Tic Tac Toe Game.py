# Tic Tac Toe Game for Two Players

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    # Check rows, columns, and diagonals
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)):
        return True

    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_full(board):
    return all(cell in ['X', 'O'] for row in board for cell in row)

def play_game():
    board = [["1", "2", "3"],
             ["4", "5", "6"],
             ["7", "8", "9"]]
    
    current_player = "X"
    moves = 0

    while True:
        print_board(board)
        move = input(f"Player {current_player}, enter the number of the cell (1-9): ")

        if not move.isdigit() or not (1 <= int(move) <= 9):
            print("Invalid input. Try again.")
            continue

        move = int(move)
        row, col = (move - 1) // 3, (move - 1) % 3

        if board[row][col] in ['X', 'O']:
            print("Cell already taken. Choose another.")
            continue

        board[row][col] = current_player
        moves += 1

        if check_winner(board, current_player):
            print_board(board)
            print(f"🎉 Player {current_player} wins!")
            break

        if is_full(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"

# Run the game
play_game()
