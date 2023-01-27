# How much will be if X is multiplied by Y if 3+x = 11-y-3 = x*y
import itertools


def are_equal(x, y):
    if 3 + x == 11 - y -3 == x * y:
        return True
    return False

for x, y in itertools.product(range(1000), range(1000)):
    if are_equal(x, y) == True:
        print(f"x = {x},  y = {y}")
        print(f"3 + x     = {3 + x}\n11 - y -3 = {11 - y -3}\nx * y     = {x * y}\n")
        