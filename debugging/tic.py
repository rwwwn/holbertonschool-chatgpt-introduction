#!/usr/bin/python3

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, symbol):
    # Check rows and columns
    for i in range(3):
        if all(cell == symbol for cell in board[i]):
            return True
        if all(board[j][i] == symbol for j in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == symbol for i in range(3)):
        return True
    if all(board[i][2 - i] == symbol for i in range(3)):
        return True
    return False

def board_full(board):
    return all(cell != " " for row in board for cell in row)

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)
        try:
            row = int(input("Enter row (0, 1, or 2) for player " + player + ": "))
            col = int(input("Enter column (0, 1, or 2) for player " + player + ": "))
            if not (0 <= row < 3 and 0 <= col < 3):
                print("Invalid coordinates. Please enter 0, 1, or 2.")
                continue
        except ValueError:
            print("Invalid input. Please enter numbers.")
            continue

        if board[row][col] != " ":
            print("That spot is already taken! Try again.")
            continue

        board[row][col] = player

        if check_winner(board, player):
            print_board(board)
            print("Player " + player + " wins!")
            break

        if board_full(board):
            print_board(board)
            print("It's a draw!")
            break

        player = "O" if player == "X" else "X"

tic_tac_toe()
