# url = "https://www.hackerrank.com/challenges/matrix-script/problem?isFullScreen=true"
"""
To decode the script, Neo needs to read each column and select only the alphanumeric characters and connect them. Neo reads the column from top to bottom and starts reading from the leftmost column.

If there are symbols or spaces between two alphanumeric characters of the decoded script, then Neo replaces them with a single space '' for better readability.

Neo feels that there is no need to use 'if' conditions for decoding.

Alphanumeric characters consist of: [A-Z, a-z, and 0-9].
"""
import math
import os
import random
import re
import sys


first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

new_list = []
for i in range(n):
    temp_transopse = ''
    for j in range(m):
        temp_transopse += matrix[j][i]
    new_list.append(temp_transopse)

print(new_list)