import numpy as np

sudoku = np.ones([5, 5], dtype=int)

sudoku[1:-1, 1:-1] = np.full((3, 3), 0)

sudoku[2, 2] = 9

print(sudoku)