n = int(input('Input number of players'))
arr = list(map(int, input().split()))
print(arr)
if (2 <= n <= 10) and (all(i in range(-100, 101) for i in arr)):
    arr.sort()
    sorted_unique_list = list(set(arr))
    print(sorted_unique_list[-2])