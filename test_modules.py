import modules_v1 as m

if __name__ =='__main__':
    grid = m.generate_sudoku()
    m.print_sudoku(grid)
    print()
    remove_grid = m.remove_numbers_from_sudoku("Hard", grid)
    m.print_sudoku(remove_grid)