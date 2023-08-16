import tkinter as tk

def is_valid(board, row, col, num):
    # Check row and column
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    # Check 3x3 box
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True

def find_empty_cell(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None, None

def solve_sudoku(board):
    row, col = find_empty_cell(board)
    if row is None or col is None:
        return True

    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num

            if solve_sudoku(board):
                return True

            board[row][col] = 0

    return False

def solve_button_callback():
    # Get the input values from the GUI
    board = [[0 for _ in range(9)] for _ in range(9)]
    for i in range(9):
        for j in range(9):
            entry_value = entry_boxes[i][j].get()
            if entry_value.isdigit():
                board[i][j] = int(entry_value)

    if solve_sudoku(board):
        # Update the GUI with the solved values
        for i in range(9):
            for j in range(9):
                entry_boxes[i][j].delete(0, tk.END)
                entry_boxes[i][j].insert(0, str(board[i][j]))
    else:
        result_label.config(text="No solution found!")

# GUI setup
root = tk.Tk()
root.title("Sudoku Solver")

entry_boxes = [[None for _ in range(9)] for _ in range(9)]
for i in range(9):
    for j in range(9):
        entry_boxes[i][j] = tk.Entry(root, width=3, font=('Helvetica', 18))
        entry_boxes[i][j].grid(row=i, column=j)

solve_button = tk.Button(root, text="Solve Sudoku", command=solve_button_callback)
solve_button.grid(row=9, column=0, columnspan=9)

result_label = tk.Label(root, text="", font=('Helvetica', 18))
result_label.grid(row=10, column=0, columnspan=9)

root.mainloop()
