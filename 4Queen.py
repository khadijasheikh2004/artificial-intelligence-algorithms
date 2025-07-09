def is_safe(board, row, col):
    # Check if there’s a queen in the same row on the left side
    for i in range(col):
        if board[row][i] == "Q":
            return False
    
    # Check the upper-left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == "Q":
            return False
    
    # Check the lower-left diagonal
    for i, j in zip(range(row, len(board)), range(col, -1, -1)):
        if board[i][j] == "Q":
            return False
    
    return True

def solve(board, col):
    # If we placed queens in all columns, the solution is complete
    if col == len(board):
        return True
    
    for row in range(len(board)):
        # Try placing the queen in each row of the current column
        if is_safe(board, row, col):
            board[row][col] = "Q"  # Place queen
            if solve(board, col + 1):  # Move to the next column
                return True
            board[row][col] = "."  # Remove queen (backtrack)
    
    return False

# Initialize an empty 4x4 board with "."
board = [["."] * 4 for _ in range(4)]

# Run the solver starting from the first column
if solve(board, 0):
    for row in board:
        print(" ".join(row))
else:
    print("No solution found")