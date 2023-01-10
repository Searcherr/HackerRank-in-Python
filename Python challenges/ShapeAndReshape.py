import numpy as np

user_array = input('Input a list of numbers: ').strip().split(' ')
my_array = np.array(user_array, int)
print(my_array)
print(np.reshape(my_array, (3, 3)))