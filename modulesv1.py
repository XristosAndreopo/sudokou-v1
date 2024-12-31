import random

""" 
    1. Check if placing a number in the grid of sudoku is valid
    2. Returns: a. True if placement is valid
                b. Returns False if placement in not valid
    3. Inputs:  a. grid: the grid we want to check if placement is valid
                b. row: the row witch the number we want to check is located
                g. col: the col witch the number we want to check is located
                d. num: The number we want to check
"""
def is_placement_valid(grid, row, col, num):
    # Check if placing num in row is valid
    if num in grid[row]:
        return False
    # Check if placing num in col is valid
    if num in [grid[i][col] for i in range(9)]:
        return False
    # Check if placing num in sub grid 3x3 is valid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if grid[i][j] == num:
                return False
    return True


""" 
    1. Check if placing a number in the cube with possible solutions is valid
    2. Returns: a. True if placement is valid
                b. Returns False if placement in not valid
    3. Inputs:  a. cube: the cube with the possible solutions.
                The cube is returned from find_possible_solutions()
                b. grid: the grid we want to check if placement is valid
                b. row: the row witch the number we want to check is located
                g. col: the col witch the number we want to check is located
"""
def is_placement_valid_in_cube(cube, row, col, num):
    # Clone Cube
    cube_clone = [
        [[0], [0], [0], [], [], [], [], [], []],
        [[0], [0], [0], [], [], [], [], [], []],
        [[0], [0], [0], [], [], [], [], [], []],
        [[], [], [], [0], [0], [0], [], [], []],
        [[], [], [], [0], [0], [0], [], [], []],
        [[], [], [], [0], [0], [0], [], [], []],
        [[], [], [], [], [], [], [0], [0], [0]],
        [[], [], [], [], [], [], [0], [0], [0]],
        [[], [], [], [], [], [], [0], [0], [0]],
    ]
    for row_clone in range(9):
        for col_clone in range(9):
                cube_clone[row_clone][col_clone] = cube[row_clone][col_clone]

    # Check if placing num in row of clone cube is valid

    # If num exist in p.x cube[1][2]
    if num in cube_clone[row][col]:
        # Delete num from entire row of cube
        for row_in_clone_cube in range(9):
            try:
                cube_clone[row_in_clone_cube][col].remove(num)
            except ValueError:
                continue

    for row_in_clone_cube in range(9):
        if not len(cube_clone[row_in_clone_cube][col]):
            return False

    # Check if placing num in column of clone cube is valid

    # If num exist in p.x cube[1][2]
    if num in cube_clone[row][col]:
        # Delete num from entire row of cube
        for col_in_clone_cube in range(9):
            try:
                cube_clone[row][col_in_clone_cube].remove(num)
            except ValueError:
                continue

    for col_in_clone_cube in range(9):
        if not len(cube_clone[row][col_in_clone_cube]):
            return False

    # Check if placing num in sub grid 3x3 is valid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    if num in cube_clone[row][col]:
        for row_in_clone_cube in range(start_row, start_row + 3):
            for col_in_clone_cube in range(start_col, start_col + 3):
                try:
                    cube_clone[row_in_clone_cube][col_in_clone_cube].remove(num)
                except ValueError:
                    continue

    for row_in_clone_cube in range(start_row, start_row + 3):
        for col_in_clone_cube in range(start_col, start_col + 3):
            if not len(cube_clone[row_in_clone_cube][col_in_clone_cube]):
                return False
    return True


""" 
    1. Randomly populate the diagonal sub grids of sudoku puzzle
       The initial sudoku grid has to be a zero grid
    2. Returns: sudoku grid with populated the diagonal sub grids
    3. Inputs:  grid: the grid we want to check if placement is valid
"""
def random_populate_diagonal_sub_grids(grid):
    sub_grid_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    sub_grid_5 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    sub_grid_9 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # Populate 1st diagonal sub grid
    for row in range(0, 3):
        for col in range(0, 3):
            grid[row][col] = random.choice(sub_grid_1)
            sub_grid_1.remove(grid[row][col])
    # Populate 2st diagonal sub grid
    for row in range(3, 6):
        for col in range(3, 6):
            grid[row][col] = random.choice(sub_grid_5)
            sub_grid_5.remove(grid[row][col])
    # # Populate 3st diagonal sub grid
    for row in range(6, 9):
        for col in range(6, 9):
            grid[row][col] = random.choice(sub_grid_9)
            sub_grid_9.remove(grid[row][col])
    return grid


""" 
    1. Create a 9x9x9 cube. The third dimension are the possible solutions.
    2. Returns: a cube with possible solutions
    3. Inputs:  grid: the grid we want to check if placement is valid
"""
def find_possible_solutions(grid):

    list_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    cube = [
        [[0], [0], [0], [], [], [], [], [], []],
        [[0], [0], [0], [], [], [], [], [], []],
        [[0], [0], [0], [], [], [], [], [], []],
        [[], [], [], [0], [0], [0], [], [], []],
        [[], [], [], [0], [0], [0], [], [], []],
        [[], [], [], [0], [0], [0], [], [], []],
        [[], [], [], [], [], [], [0], [0], [0]],
        [[], [], [], [], [], [], [0], [0], [0]],
        [[], [], [], [], [], [], [0], [0], [0]],
    ]
    # Populate cube
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                for num in list_numbers:
                    if is_placement_valid(grid, row, col, num):
                        cube[row][col].append(num)
    return cube

""""
    1. Removes the a number from possible solutions of row, col and sub gid
    2. Return's cube with removed numbers
    3. Input:   a. cube: cube with possible solutions
                b. row: the row of number
                g. col: the col of number
                d. num: the num we want to remove 
"""
def remove_same_numbers_from_cube(cube, row, col, num):
    # Remove same numbers from row
    if num in cube[row][col]:
        for row_in_cube in range(9):
            try:
                cube[row_in_cube][col].remove(num)
            except ValueError:
                continue
    # Remove same numbers from col
    if num in cube[row][col]:
        for col_in_cube in range(9):
            try:
                cube[row][col_in_cube].remove(num)
            except ValueError:
                continue
    # Remove same numbers for sub grid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for row_of_sub in range(start_row, start_row + 3):
        for col_of_sub in range(start_col, start_col + 3):
            try:
                cube[row_of_sub][col_of_sub].remove(num)
            except ValueError:
                continue
    print("remove_same_numbers_from_cube")
    for row in range(9):
        print(cube[row])
    return cube

"""
    1. Populate sudoku grid with random numbers from 1 to 9. It implements 
    function random_populate_diagonal_sub_grids()
    2. Return's the sudoku grid filled with numbers
    3. Inputs:  grid: the grid we want to fill with numbers
"""
def fill_grid(grid):
    # Call functions to randomly populate grid
    filled_grid = random_populate_diagonal_sub_grids(grid)
    # Call function to generate cube with possible solutions
    cube = find_possible_solutions(filled_grid)
    # Create a list from 1 to 9 and shuffle it
    list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    random.shuffle(list_of_numbers)
    for row in range(9):
        print(cube[row])
        print("-------")
    print(list_of_numbers)
    for row in range(9):
        for col in range(9):
            # Find Empty Cells
            if filled_grid[row][col] == 0:
                for num in list_of_numbers:
                    if is_placement_valid_in_cube(cube, row, col, num):
                        print("is valid")
                        filled_grid[row][col] = num
                        print(num)
                        cube = remove_same_numbers_from_cube(cube, row, col, num)
                        try:
                            cube[row][col].remove(num)
                            print("--1--")
                            for row111 in range(9):
                                print(cube[row])
                            print("--1--")

                            print(cube)
                            break
                        except ValueError:
                            continue
    return filled_grid


"""
    1. Main function of modules.py. Generate our sudoku grid
    2. Return:  a. Random Sudoku Grid if is_filled() is true
                b. Zero Sudoku Grid if is_filled() is False
    3. Inputs:  None
"""
def generate_sudoku():
    # Create a zero sudoku grid
    sudoku_grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    filled_grid = fill_grid(sudoku_grid)
    return filled_grid


def print_sudoku(grid):
    for i in range(9):
        if i % 3 == 0 and i != 0:  # Horizontal block border
            print("-" * 21)
        for j in range(9):
            if j % 3 == 0 and j != 0:  # Vertical block border
                print("| ", end="")
            print(grid[i][j] if grid[i][j] != 0 else ".", end=" ")
        print()  # New line after each row

