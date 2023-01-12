import numpy as np

#user_shape = np.array(input('Enter the shape of your matrix: ').strip().split(' '), int)
#print(type(user_shape))
user_shape = input('Enter the shape of your matrix: ')
user_shape_tuple = tuple(int(item) for item in user_shape.split())
print(user_shape_tuple)

user_zeros_matrix = np.zeros(user_shape_tuple)
user_ones_matrix = np.ones(user_shape_tuple)
print(user_zeros_matrix)
print(user_ones_matrix)