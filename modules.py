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
    #Check if placing num in sub grid 3x3 is valid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row,start_row+3):
        for j in range(start_col,start_col+3):
            if grid[i][j] == num:
                return False
    return True


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
    for row in range(0,3):
        for col in range(0,3):
            grid[row][col] = random.choice(sub_grid_1)
            sub_grid_1.remove(grid[row][col])
    # Populate 2st diagonal sub grid
    for row in range(3,6):
        for col in range(3,6):
            grid[row][col] = random.choice(sub_grid_5)
            sub_grid_5.remove(grid[row][col])
    # # Populate 3st diagonal sub grid
    for row in range(6,9):
        for col in range(6,9):
            grid[row][col] = random.choice(sub_grid_9)
            sub_grid_9.remove(grid[row][col])
    return grid


""" 
    1. Randomly populate a sub grid of sudoku puzzle
       The initial sudoku grid has to be a zero grid
    2. Returns: sudoku grid with populated the sub grid
    3. Inputs:  grid: the grid we want to check if placement is valid
"""

def random_populate_sub_grid(grid, start_row, start_col):
    list_number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # Populate 3nd sub grid
    for row in range(start_row,start_row+3):
        for col in range(start_col,start_col+3):
            num = random.choice(list_number)
            if is_placement_valid(grid, row, col, num):
                grid[row][col] = num
                list_number.remove(num)
    if check_subgrid_has_zero(grid, start_row, start_col):
        # uncomment next line to see number of recursions
        # print("recursion")
        random_populate_sub_grid(grid, start_row, start_col)
    return grid

"""
    1. Populate sudoku grid with random numbers from 1 to 9. It implements 
    function random_populate_diagonal_sub_grids()
    2. Return's the sudoku grid filled with numbers
    3. Inputs:  grid: the grid we want to fill with numbers
"""
def fill_grid(grid):
    try:
        # Call functions to randomly populate grid
        filled_grid = random_populate_diagonal_sub_grids(grid)
        filled_grid = random_populate_sub_grid(filled_grid, 0, 6)
        filled_grid = random_populate_sub_grid(filled_grid, 6,0)
        filled_grid = random_populate_sub_grid(filled_grid, 0,3)
        filled_grid = random_populate_sub_grid(filled_grid, 3, 0)
        filled_grid = random_populate_sub_grid(filled_grid, 6, 3)
        filled_grid = random_populate_sub_grid(filled_grid, 3, 6)
    except RecursionError:
        fill_grid(grid)
        # uncomment next line to see number of recursions
        # print("Second Row of recursions")
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


# Remove numbers for the sudoku grid according to level and place 0
# return a grid for player to play with some cells set to 0

# PREPEI NA TO KSANADW GT PREPEI NA SIGOYRECV OTI MPORW NA BRW TH LYSH\

def remove_numbers(sudoku_grid, level):
    # Setting the amount of cells to be removed according to level
    difficulty = {
        "Easy": 35,
        "Advanced": 45,
        "Expert": 60
    }
    removed_numbers_sudoku = sudoku_grid
    # For amount of cells to be deleted
    while difficulty[level] > 0:
        # Generate random row and column
        row, col = random.randint(0, 8), random.randint(0, 8)
        # If the cell is not 0
        if removed_numbers_sudoku[row][col] != 0:
            # Set the cell to 0
            removed_numbers_sudoku[row][col] = 0
            # Decrease the amount of cells to be removed be one
            difficulty[level] -= 1
    return removed_numbers_sudoku

# Set a zero cell to player's number of choice
# Returns updated players grid
def update_player_grid(original_grid, player_grid_to_be_updated, row, col, player_number):
    if original_grid[row][col] == 0:
        player_grid_to_be_updated[row][col] = player_number
    else:
        print("This move is invalid")
    return player_grid_to_be_updated


# If grid is the same as player_grid the puzzle is solved
# Returns True if all cells are populated and the two grids are a match
# Returns False if all cells are populated and the two grids are no match
def is_solved(original_grid, solved_player_grid):
    for row in range(9):
        for col in range(9):
            if original_grid[row][col] != solved_player_grid[row][col]:
                return False
    return True

# implement player moves, B4 9, undo, reset

def print_sudoku(grid):
    for i in range(9):
        if i % 3 == 0 and i != 0:  # Horizontal block border
            print("-" * 21)
        for j in range(9):
            if j % 3 == 0 and j != 0:  # Vertical block border
                print("| ", end="")
            print(grid[i][j] if grid[i][j] != 0 else ".", end=" ")
        print()  # New line after each row

