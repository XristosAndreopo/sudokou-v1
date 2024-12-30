import modules as m

if __name__ =='__main__':
    grid = m.generate_sudoku()
    for row in range(9):
        print(grid[row])
    #print(grid)
    level = input("Please choose Easy, Advance, Expert to set the level of sudoku:")
    player_grid = m.remove_numbers(grid, level=level)
    print(grid)
    print(player_grid)
    m.print_sudoku(player_grid)
    play = True
    while play:
        player_row = int(input("Enter a row between 1 to 9:"))-1
        player_col = int(input("Enter a column between 1 to 9:"))-1
        player_number = input("Enter a number between 1 to 9:")
        player_grid = m.update_player_grid(grid, player_grid, player_row, player_col, player_number)
        if m.is_solved(grid, player_grid):
            print("Congratulations! You Solved the Puzzle")
            play = False
        m.print_sudoku(player_grid)

# check the grids - there is a logic mistake