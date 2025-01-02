# Sudoku Game web app - Version 1

## About The Project
This is a basic implementation of the classic sudoku game.

### Built With
This project was build with:
1) Pycharm 
2) and Streamlit

### Prerequisites
 
Read Instructions.txt

### Logic of Back End
The task is to generate a 9 x 9 Sudoku grid having k empty cells while following
the below set of **rules**:

1. In all 9 submatrices 3×3, the elements should be 1-9, without repetition.
2. In all rows, there should be elements between 1-9, without repetition.
3. In all columns, there should be elements between 1-9, without repetition.

In 9x9 matrix, the diagonal matrices are independent of other empty matrices
initially.

Approach:

1. Fill all the diagonal 3×3 matrices.
2. Fill recursively the two matrices (not the ones in the diagonal line), which
are located in the top right and bottom left. 
We pick these two because, since the diagonal matrices are filled, the maximum
number of rules above are met. So we achieve minimum recursions with the right
numbers placed in cells.
3. Generate a cube, 9x9x9 with possible solutions
4. Loop through the cube and if cube[i][j] has len 1, there is one possible 
solution, so we place it in sudoku puzzle. Generate again a cube with possible
solutions. We loop through 36 times because if we pass the second step 
36 cells remain empty.
5. Fill rest of remaining cells, picking a number from the last cube with
possible solutions, which met the criteria of the rules.
6. If 9x9 grid has a zero, populate the grid again from step 1 to 5.
7. If sum of rows and columns is not 45, populate the grid again from step 1
to 5.


### Installation

1. Clone the repo with the
```sh
  https://github.com/XristosAndreopo/sudokou-v1.git
   ```

<!-- CONTACT -->
## Contact

Christos - xristos.andreopo@gmail.com

Project Link: https://github.com/XristosAndreopo/sudokou-v1.githttps://github.com/your_username/repo_name)

