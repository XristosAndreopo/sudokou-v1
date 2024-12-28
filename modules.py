import random


# Check if placing a number in the grid of sudoku is valid
# Returns True if placement is valid
# Returns False if placement in not valid
def is_placement_valid(rand_grid, row, col, num):

    # Check if placing num in row is valid
    if num in rand_grid[row]:
        return False

    # Check if placing num in col is valid
    if num in [rand_grid[i][col] for i in range(9)]:
        return False

    #Check if placing num in sub grid 3x3 is valid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row,start_row+3):
        for j in range(start_col,start_col+3):
            if rand_grid[i][j] == num:
                return False
    return True

# Populate sudoku grid with random numbers from 1 to 9
# Returns True if the grid is populated
# Returns False if the grid is not populated
def fill_grid(random_grid):
    # Populate the grid with random numbers between 1 and 9
    # Loop through rows
    for row in range(9):
        # Loop through columns
        for col in range(9):
            # Find empty cell
            if random_grid[row][col] == 0:
                #try numbers in random order
                for num in random.sample(range(1, 10), 9):
                    if is_placement_valid(random_grid, row, col, num):
                        random_grid[row][col] = num
                        #Because we will get zeros in grid due to randomness
                        #we call the function again
                        if fill_grid(random_grid):
                            return True
                        random_grid[row][col] = 0
                return False
    return True


# Generate the sudoku grid from a zero grid, implementing
# def fill_grid(random_grid) function
# Returns a list 9 x 9 as the grid of a sudoku puzzle
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
    # Call the function to fill the grid to get our sodoku_grid
    fill_grid(sudoku_grid)

    return sudoku_grid

# Remove numbers for the sudoku grid according to level and place 0
# return a grid for player to play with some cells set to 0
def remove_numbers(sudoku_grid, level):
    # Setting the amount of cells to be removed according to level
    difficulty = {
        "Easy": 35,
        "Advance": 45,
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

#implement player moves, B4 9, undo, reset

def print_sudoku(grid):
    for i in range(9):
        if i % 3 == 0 and i != 0:  # Horizontal block border
            print("-" * 21)
        for j in range(9):
            if j % 3 == 0 and j != 0:  # Vertical block border
                print("| ", end="")
            print(grid[i][j] if grid[i][j] != 0 else ".", end=" ")
        print()  # New line after each row

if __name__ =='__main__':
    grid = generate_sudoku()
    print(grid)
    level = input("Please choose Easy, Advance, Expert to set the level of sudoku:")
    player_grid = remove_numbers(grid, level=level)
    print(grid)
    print(player_grid)
    print_sudoku(player_grid)
    play = True
    while play:
        player_row = int(input("Enter a row between 1 to 9:"))-1
        player_col = int(input("Enter a column between 1 to 9:"))-1
        player_number = input("Enter a number between 1 to 9:")
        player_grid = update_player_grid(grid, player_grid, player_row, player_col, player_number)
        if is_solved(grid, player_grid):
            print("Congratulations! You Solved the Puzzle")
            play = False
        print_sudoku(player_grid)