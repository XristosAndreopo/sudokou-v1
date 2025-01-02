import random
import copy

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
    for i in range(9):
        if num == grid[row][i]:
            return False
    # Check if placing num in col is valid
    for i in range(9):
        if num == grid[i][col]:
            return False
    #Check if placing num in sub grid 3x3 is valid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row,start_row+3):
        for j in range(start_col,start_col+3):
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
# we dont use it
def is_placement_valid_in_cube(cube, row, col, num):

    #Check if num is not in p.x.cube_cone[0][3]
    if num not in cube[row][col]:
        return False
    # If number in p.x. cube_clone[0][3]
    # Clone Cube
    cube_clone = copy.deepcopy(cube)
    # Check if placing num in row of clone cube is valid
    # Delete num from entire row of cube
    for col_in_clone_cube in range(9):
        try:
            cube_clone[row][col_in_clone_cube].remove(num)
        except ValueError:
            continue
    for col_in_clone_cube in range(9):
        if not len(cube_clone[row][col_in_clone_cube]):
            return False
    # Check if placing num in column of clone cube is valid
    # Delete num from entire row of cube
    for row_in_clone_cube in range(9):
        try:
            cube_clone[row_in_clone_cube][col].remove(num)
        except ValueError:
            continue

    for row_in_clone_cube in range(9):
        if not len(cube_clone[row_in_clone_cube][col]):
            return False
    # Check if placing num in sub grid 3x3 is valid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
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
    1. Checks if a subgrid has zeros
    2. Returns: a. True if it has at least one zero
                b. False if it has no zeros 
    3. Inputs:  a. grid: the grid we want to check
                b. row: the start row of subgrid
                g. col: the start col of subgrid
"""
def check_subgrid_has_zero(grid, row, col):
    for i in range(row, row+3):
        for j in range(col, col+3):
            if grid[i][j] ==0:
                return True
    return False

""" 
    1. Randomly populate a sub grid of sudoku puzzle
       The initial sudoku grid has to be a zero grid
    2. Returns: sudoku grid with populated the sub grid
    3. Inputs:  grid: the grid we want to check if placement is valid
"""

def random_populate_sub_grid(grid, start_row, start_col):
    list_number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    random.shuffle(list_number)
    # Populate random sub grid
    for row in range(start_row,start_row+3):
        for col in range(start_col,start_col+3):
            for num in list_number:
                if is_placement_valid(grid, row, col, num):
                    grid[row][col] = num
                    list_number.remove(num)
                    break
    if check_subgrid_has_zero(grid, start_row, start_col):
        random_populate_sub_grid(grid, start_row, start_col)
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
    for row_in_cube in range(9):
        try:
            cube[row_in_cube][col].remove(num)
        except ValueError:
            continue
    # Remove same numbers from col
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
    return cube

"""
    1. Check's if grid is fully populated
    2. Return:  a. True if grid is not populated and has zeros
                b. False if grid is fully populated without zeros
    3. Input:   a. grid: the grid we want to check
"""
def has_grid_zero(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                return True
    return False

"""
    1. Check's if cube has unique solutions and place them on grid
    2. Return:  a. grid of sudoku puzzle
    3. Input:   a. grid: the grid we want to check
                b. cube: cube with possible solutions
"""
def place_unique_solutions_from_cube(grid,cube):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                if len(cube[row][col]) == 1:
                    grid[row][col] = cube[row][col][0]
    return grid
"""
    1. Populate sudoku grid with random numbers from 1 to 9. It implements 
    function random_populate_diagonal_sub_grids()
    2. Return the sudoku grid filled with numbers
    3. Inputs:  grid: the grid we want to fill with numbers
"""
def fill_grid(grid):
    # Call functions to randomly populate sub grids
    grid = random_populate_diagonal_sub_grids(grid)
    grid = random_populate_sub_grid(grid, 0, 6)
    grid = random_populate_sub_grid(grid, 6, 0)
    for i in range(81):
        cube = find_possible_solutions(grid)
        grid = place_unique_solutions_from_cube(grid, cube)
    cube = find_possible_solutions(grid)
    for row in range(9):
        for col in range(9):
            # Find Empty Cells
            if grid[row][col] == 0:
                for num in cube[row][col]:
                    if is_placement_valid(grid, row, col, num):
                        grid[row][col] = num
                        cube = remove_same_numbers_from_cube(cube, row, col, num)
                        break
    return grid

"""
    1. Check if sum of row/column is 45
    2. Return:  a. True if sum of row/column is not 45
                b. False if sum of row/column is 45
    3. Input:   a. grid: the grid we want to check
"""
def has_not_45_sums(grid):
    list_row=[0,0,0,0,0,0,0,0,0]
    list_col=[0,0,0,0,0,0,0,0,0]

    for row in range(9):
        for col in range(9):
            list_row[row] = list_row[row] + int(grid[row][col])
            list_col[row] = list_col[row] + int(grid[col][row])

    for i in range(9):
        if list_row[i] != 45:
            return True
        if list_col[i] !=45:
            return True
    return False

"""
    1. Main function of modules.py. Generate our sudoku grid
    2. Return:  a. Sudoku Grid 
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
    # Call function to fill the grid
    sudoku_grid = fill_grid(sudoku_grid)
    if has_grid_zero(sudoku_grid):
        sudoku_grid = generate_sudoku()
    if has_not_45_sums(sudoku_grid):
        sudoku_grid = generate_sudoku()

    return sudoku_grid


