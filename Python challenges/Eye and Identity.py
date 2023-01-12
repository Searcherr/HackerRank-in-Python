import numpy as np
np.set_printoptions(legacy='1.13')

N, M = map(int, input('Enter the shape of the matrix: ').split())
#user_indentity_matrix = np.identity(N)
output_matrix = np.eye(N, M, k=0)

print(output_matrix)