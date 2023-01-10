import numpy as np

def arrays(arr):
    # complete this function
    # use numpy.array
    my_array = np.array(arr, float)
    return np.flip(my_array)
arr = input('Input a list of numbers: ').strip().split(' ')
result = arrays(arr)
print(result)