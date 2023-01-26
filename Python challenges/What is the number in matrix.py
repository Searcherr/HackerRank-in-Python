"""
2 7 ? = X
? ? 1 = X
4 ? 8 = X
= = =
X X X
"""
from itertools import permutations 
import numpy as np


n = 0
matrix = np.array([[2, 7, n],
                [n, n, 1],
                [4, n, 8]])
numbers = (3, 5, 6, 9)

print(matrix)

perm = permutations([3, 5, 6, 9]) 


for i in list(perm): 
    matrix[0][2] = i[0]
    matrix[1][0] = i[1]
    matrix[1][1] = i[2]
    matrix[2][1] = i[3]

    #print(np.sum(matrix[0]), np.sum(matrix[1]), np.sum(matrix[2]), sep=' ')
    if np.sum(matrix[0]) == np.sum(matrix[1]) == np.sum(matrix[2]) == \
        matrix.sum(axis=0)[0] == matrix.sum(axis=0)[1] == matrix.sum(axis=0)[2] == \
        np.trace(matrix):
        print(f"Sum = {np.sum(matrix[0])}")
        print(matrix[0][2], matrix[1][0], matrix[1][1], matrix[2][1], sep=' ')
        