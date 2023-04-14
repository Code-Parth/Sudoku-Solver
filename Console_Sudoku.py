def solve_sudoku(board):
    # Find the next empty cell in the board
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                # Try to fill the cell with every possible number
                for num in range(1, 10):
                    if is_valid(board, i, j, num):
                        board[i][j] = num
                        # Recursively try to fill the rest of the board
                        if solve_sudoku(board):
                            return True
                        # If we couldn't solve the board with this number, backtrack
                        board[i][j] = 0
                # If we've tried every number and couldn't solve the board, return False
                return False
    # If there are no more empty cells, the board is solved!
    return True


def is_valid(board, row, col, num):
    # Check if the number is already in the same row or column
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    # Check if the number is already in the same 3x3 box
    box_row = row // 3 * 3
    box_col = col // 3 * 3
    for i in range(box_row, box_row + 3):
        for j in range(box_col, box_col + 3):
            if board[i][j] == num:
                return False
    # If the number is not already in the same row, column, or box, it is valid
    return True


# Example board
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# Solve the board
solve_sudoku(board)

# Print the solved board
for row in board:
    print(row)
