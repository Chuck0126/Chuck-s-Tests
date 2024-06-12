def reverse_list(l: list):

    reversed_list = []
    for item in l:
        reversed_list.insert(0, item)
    return reversed_list


def solve_sudoku(matrix):
    def is_valid(num, pos):
        # Check the row
        for i in range(len(matrix[0])):
            if matrix[pos[0]][i] == num and pos[1] != i:
                return False

        # Check the column
        for i in range(len(matrix)):
            if matrix[i][pos[1]] == num and pos[0] != i:
                return False

        # Check the 3x3 subgrid
        box_x = pos[1] // 3
        box_y = pos[0] // 3
        for i in range(box_y*3, box_y*3 + 3):
            for j in range(box_x*3, box_x*3 + 3):
                if matrix[i][j] == num and (i, j) != pos:
                    return False

        return True

    def solve():
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    for num in range(1, 10):
                        if is_valid(num, (i, j)):
                            matrix[i][j] = num
                            if solve():
                                return True
                            matrix[i][j] = 0
                    return False
        return True

    solve()

# Test the function with an unsolved sudoku puzzle
sudoku = [
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

solve_sudoku(sudoku)

# Print the solved sudoku puzzle
for row in sudoku:
    print(row)
