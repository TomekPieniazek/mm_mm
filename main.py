sudoku_board = [
    [3, 7, 0, 1, 4, 0, 9, 6, 0],
    [0, 2, 9, 6, 7, 3, 1, 0, 0],
    [0, 0, 0, 0, 9, 0, 0, 7, 4],
    [0, 0, 2, 5, 0, 0, 0, 0, 0],
    [7, 4, 0, 0, 0, 0, 0, 0, 8],
    [1, 0, 0, 0, 2, 0, 7, 0, 0],
    [9, 0, 0, 7, 6, 2, 0, 3, 1],
    [0, 5, 7, 3, 0, 1, 6, 0, 9],
    [6, 1, 0, 0, 0, 0, 0, 0, 7]
]


def print_sudoku(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - ")
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            print(board[i][j], end=" ")
        print()


def possibilities_on_line(board, row, column):
    rows = []
    columns = []
    # Print in row
    for i in range(len(board[row])):
        columns.append(board[row][i])

    for i in range(len(board)):
        rows.append(board[i][column])

    missing_numbers = sorted(list(set(range(10)) - set(rows) - set(columns)))
    return missing_numbers


def get_box_indices(row, col):
    box_row = row // 3
    box_col = col // 3
    return box_row, box_col


def possibilities_in_box(board, row, col):
    box_row, box_col = get_box_indices(row, col)
    box_values = []

    for i in range(box_row * 3, (box_row + 1) * 3):
        for j in range(box_col * 3, (box_col + 1) * 3):
            box_values.append(board[i][j])

    missing_numbers = sorted(list(set(range(1, 10)) - set(box_values)))
    return missing_numbers


def change_number(row, column, number, board):
    board[row][column] = number
    return board


def is_valid(board, row, col, num):
    for x in range(9):
        if board[row][x] == num:
            return False

    for x in range(9):
        if board[x][col] == num:
            return False

    start_row, start_col = row - row % 3, col - col % 3
    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == num:
                return False

    return True


def solve_sudoku(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                possibilities = possibilities_on_line(board, i, j)
                box_possibilities = possibilities_in_box(board, i, j)
                missing_numbers = sorted(list(set(range(10)) - set(possibilities) - set(box_possibilities)))
                if len(missing_numbers) == 1:
                    board = change_number(i, j, missing_numbers[0], board)
                print(missing_numbers)
    return board
    # return solve_sudoku(board)


print_sudoku(solve_sudoku(sudoku_board))
