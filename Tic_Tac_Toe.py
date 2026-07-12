def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    # Rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Diagonals
    if all(board[i][i] == player for i in range(3)):
        return True

    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

board = [[" " for _ in range(3)] for _ in range(3)]
current = "X"

for turn in range(9):
    print_board(board)

    while True:
        row = int(input(f"{current} Row (0-2): "))
        col = int(input(f"{current} Col (0-2): "))

        if board[row][col] == " ":
            board[row][col] = current
            break
        else:
            print("Cell already occupied!")

    if check_winner(board, current):
        print_board(board)
        print(f"{current} Wins!")
        break

    current = "O" if current == "X" else "X"
else:
    print_board(board)
    print("It's a Draw!")
