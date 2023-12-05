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


def is_valid(board):
    if 0 not in board[0] and 0 not in board[1] and 0 not in board[2] and 0 not in board[3] and 0 not in board[4] and 0 not in board[5] and 0 not in board[6] and 0 not in board[7] and 0 not in board[8]:
        return True
    else:
        return False



def solve_sudoku(board):

    if is_valid(board):
        return board

    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                possibilities = possibilities_on_line(board, i, j)
                box_possibilities = possibilities_in_box(board, i, j)
                print(possibilities)
                print(box_possibilities)
                missing_numbers = [value for value in possibilities if value in box_possibilities]
                print(missing_numbers)
                print('---------------------------')
                if len(missing_numbers) == 1:
                    board = change_number(i, j, missing_numbers[0], board)
                    print('Board has been changed')
    return solve_sudoku(board)


print_sudoku(solve_sudoku(sudoku_board))
