"""
You are given a NxM integer array matrix with space separated elements (N= rows and M= columns).
Your task is to print the transpose and flatten results.

"""
import numpy as np

N, M = map(int, input('Enter the shape of your matrix: ').split())
user_array = np.zeros((N, M))

def string_to_raw(user_raw):
    return np.array(user_raw, int)

i = 0
while i < N:
    current_raw_str = input(f"Input raw number {i+1}: ").strip().split(' ')
    current_raw_np = string_to_raw(current_raw_str)
    for j in range(M):
        user_array[i, j] = int(current_raw_np[j])
    i += 1

print(user_array.transpose().astype(int))
print(user_array.flatten().astype(int))