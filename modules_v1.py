import random
import copy
"""
-----------------------Generate Sudoku Puzzle-----------------------------------
"""
def is_placement_valid(grid, row, col, num):
    """
    Check if placing a number in the grid of sudoku is valid
    :param grid: the grid we want to check if placement is valid
    :param row: the row witch the number we want to check is located
    :param col: the col witch the number we want to check is located
    :param num: The number we want to check
    :return: True if placement is valid, False if placement in not valid
    """
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

def random_populate_diagonal_sub_grids(grid):
    """
    Randomly populate the diagonal sub grids of sudoku puzzle. The initial
    sudoku grid has to be a zero grid.
    :param grid: the grid we want to populate the diagonal sub grids
    :return: sudoku grid with populated the diagonal sub grids
    """
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

def check_subgrid_has_zero(grid, row, col):
    """
    Checks if a subgrid has zeros
    :param grid: the grid we want to check
    :param row: the start row of subgrid
    :param col: the start col of subgrid
    :return: True if it has at least one zero, False if it has no zeros
    """
    for i in range(row, row+3):
        for j in range(col, col+3):
            if grid[i][j] ==0:
                return True
    return False

def random_populate_sub_grid(grid, start_row, start_col):
    """
    Randomly populate a sub grid of sudoku puzzle.
    :param grid: the grid we want to populate
    :param start_row: the start of row of subgrid
    :param start_col: the start of col of subgrid
    :return: sudoku grid with populated the sub grid
    """
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

def remove_same_numbers_from_cube(cube, row, col, num):
    """
    Removes the number from possible solutions of row, col and sub gid.
    :param cube: cube with possible solutions.
    :param row: the row of number.
    :param col: the column of number.
    :param num: the num we want to remove.
    :return: cube with removed number from possible solutions.
    """
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

def fill_grid(grid):
    """
    Populate sudoku grid with numbers from 1 to 9.
    :param grid: the grid we want to fill with numbers
    :return: Return the sudoku grid filled with numbers
    """
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

def has_not_45_sums(grid):
    """
    Check if sum of row/column is 45.
    :param grid: the grid we want to check.
    :return: True if sum of row/column is not 45, False if sum of row/column is
    45.
    """
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

def find_possible_solutions(grid):
    """
    Create a 9x9x9 cube. The third dimension are the possible solutions.
    :param grid: the grid we want to find the possible solutions of.
    :return: a cube with possible solutions.
    """
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

def place_unique_solutions_from_cube(grid,cube):
    """
    Check's if cube with possible solutions has unique solutions and place them
    in sudoku grid.
    :param grid: the grid we want to place unique solutions.
    :param cube: cube with possible solutions.
    :return: grid of sudoku puzzle.
    """
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                if len(cube[row][col]) == 1:
                    grid[row][col] = cube[row][col][0]
    return grid

def has_grid_zero(grid):
    """
    Check's if sudoku grid is fully populated.
    :param grid: the grid we want to check.
    :return: True if grid is not populated and has zeros, False if grid is fully
    populated without zeros.
    """
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                return True
    return False

def generate_sudoku():
    """
    Main function of Generate Sudoku Puzzle in modules_v1.py. Generate sudoku
    grid.
    :return: Sudoku Grid fully populated.
    """
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

"""
-----------------Creating the Sudoku with Removed numbers-----------------------
"""

def has_sudoku_grid_solution(grid):
    """
    Check's if sudoku grid can be fully populated by only unique solutions.
    :param grid: the grid with the removed numbers.
    :return: True if it can be solved(is fully populated), False if it can not
    be solved(is not fully populated).
    """
    # Create a deep copy of grid
    clone_sudoku_grid = copy.deepcopy(grid)
    # Place unique solutions from generated cube with possible solutions
    for i in range(31):
        cube = find_possible_solutions(clone_sudoku_grid)
        # Remove zeros from cube
        for row in range(9):
            for col in range(9):
                if 0 in cube[row][col]:
                    cube[row][col].remove(0)
        clone_sudoku_grid = place_unique_solutions_from_cube(clone_sudoku_grid,cube)
    # If after placing all unique solutions, grid still has zeros return false
    if has_grid_zero(clone_sudoku_grid):
        return False
    return True

def remove_numbers_from_sudoku(level, sudoku_grid):
    """
    Removes number from sudoku according to level
    :param level: Easy, Medium, Hard, Expert
    :param sudoku_grid: The grid we want to remove numbers from
    :return: sudoku grid with removed numbers
    """
    # Make a copy of the sudoku grid
    clone_sudoku_grid = copy.deepcopy(sudoku_grid)
    # Set the difficulty and how many numbers should be removed
    level_of_sudoku = {"easy": 28,
                       "medium": 36,
                       "hard": 50,
                       "expert": 50 #different method of removing numbers
    }
    # If level is Easy or Medium or Hard remove numbers
    if level.lower() == "easy" or level.lower() == "medium" or level.lower()=="hard":
        while level_of_sudoku[level.lower()] > 0:
            cell_id = random.randint(0, 80)
            row = cell_id // 9
            col = cell_id % 9
            if clone_sudoku_grid[row][col] !=0 and clone_sudoku_grid[col][row] !=0:
                clone_sudoku_grid[row][col] = 0
                clone_sudoku_grid[col][row] = 0
                level_of_sudoku[level.lower()] = level_of_sudoku[level.lower()] - 2
        # Check if a solution can be found
        if not has_sudoku_grid_solution(clone_sudoku_grid):
            clone_sudoku_grid = remove_numbers_from_sudoku(level, sudoku_grid)
        return clone_sudoku_grid

"""
--------------------------Checks of Player Inputs-------------------------------
"""

def check_input_level_of_difficulty(user_input):
    """
    Check if users input is Easy/Medium/Hard.
    :param user_input: the input of the player.
    :return: True if input is Easy/Medium/Hard, False if input is not Easy/
    Medium/Hard.
    """
    if user_input not in ["Easy", "Medium", "Hard"]:
        print("Please select between Easy/Medium/Hard")
        return False
    return True

def check_input_number(user_input):
    """
    Check if users input is between 1 and 9.
    :param user_input: the input of the player.
    :return: True if input is between 1 and 9, False if input is between 1 and 9.
    """
    if  int(user_input) > 9 or int(user_input) < 1:
        print("Please select a number between 1 to 9!")
        return False
    return True

"""
-------------------------------Player Inputs------------------------------------
"""

def player_input_difficulty():
    """
    Player set the difficulty of sudoku puzzle (Easy/Medium/Hard).
    :return: difficulty level of sudoku puzzle.
    """
    while True:
        difficulty_level = input(
            "Please select level of difficulty (Easy/Medium/Hard):")
        if check_input_level_of_difficulty(difficulty_level):
            return difficulty_level

def player_input_number():
    """
    Player set the number of number, row or column
    :return: return number of choice of player
    """
    while True:
        input_number = input("Please select a number between 1 to 9: ")
        if check_input_number(input_number):
            return int(input_number)

"""
------------------------------Player Gameplay-----------------------------------
"""

def is_the_play_valid(grid, removed_numbers_grid, num, row, col):
    """
    Return's if play of player is valid or not.
    :param grid: the grid we want to check that is fully populates.
    :param removed_numbers_grid: the grid with the removed numbers.
    :param num: the number which the player wishes to play.
    :param row: the row that the number is located.
    :param col: the column that the number is located.
    :return: True if play of player is valid, False if play of player is not
    valid.
    """
    if removed_numbers_grid[row][col] == 0:
        if grid[row][col] == num:
            return True
    else:
        print("There is a number in this location.")
    return False

def update_sudoku_grid(grid, removed_numbers_grid, num, row, col):
    """
    Set the number, the player want to make, to the grid with the removed
    numbers, if the play is valid.
    :param grid: the grid that was generated.
    :param removed_numbers_grid: the grid that the numbers are removed and the
    player want to solve.
    :param num: the choice of the number of the player that he wants to play.
    :param row: the row in which player want to play the number.
    :param col: the row in which player want to play the number.
    :return: updated_sudoku_grid.
    """
    # If play the player want to make is valid
    if is_the_play_valid(grid, removed_numbers_grid,num,row,col):
        removed_numbers_grid[row][col] = num
    else:
        print("The play is not valid")
    return removed_numbers_grid

# def undo_play():

def gameplay():
    """
    The main function of Player Gameplay in modules_v1.py. Generates sudoku grid,
    sudoku grid with removed numbers, handles input of player and stops when
    sudoku puzzle with removed numbers is solved.
    :return:
    """
    grid = generate_sudoku()
    # Player sets level of difficulty
    difficulty_level = player_input_difficulty()
    # Create grid with removed numbers
    grid_removed_numbers = remove_numbers_from_sudoku(difficulty_level, grid)
    print_sudoku(grid_removed_numbers)
    # Main loop of game
    while has_grid_zero(grid_removed_numbers):
        # Player inputs
        player_number = player_input_number()
        print("For row:")
        player_row = player_input_number() -1
        print("For col:")
        player_col = player_input_number() -1
        if is_the_play_valid(grid, grid_removed_numbers, player_number,player_row, player_col):
            grid_removed_numbers[player_row][player_col] = player_number
        print_sudoku(grid_removed_numbers)


"""
------------------------Basic Print in Formatted Style--------------------------
"""
def print_sudoku(grid):
    """
    Prints the Sudoku grid in a formatted style with position indicators.
    Generated with ChatGPT.
    :param grid: A 9x9 list of lists representing the Sudoku grid.
    """
    # Print the top row numbers
    print("    " + " ".join(f"{i+1} " if (i+1) % 3 != 0 else f"{i+1}| " for i in range(9)))
    print("  " + "-" * 29)  # Top border separator

    for row_index, row in enumerate(grid):
        # Print row number at the start
        print(f"{row_index + 1} |", end=" ")

        for col_index, num in enumerate(row):
            # Separator between 3x3 blocks
            if col_index % 3 == 0 and col_index != 0:
                print("|", end=" ")

            # Print the cell value or '.' for empty cells
            print(f"{num if num != 0 else '.'} ", end="")

        print()  # Newline after each row

        # Separator after every 3 rows
        if (row_index + 1) % 3 == 0 and row_index != 8:
            print("  " + "-" * 29)

