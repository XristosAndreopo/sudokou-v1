import modulesv1 as m

if __name__ =='__main__':
    grid = m.generate_sudoku()
    for row in range(9):
        print(grid[row])
    #print(grid)