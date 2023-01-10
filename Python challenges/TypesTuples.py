import builtins


if __name__ == '__main__':
    n = int(input('Input the range of the tuple: '))
    user_numbers = input(f"Enter {n} numbers: ")
    strings_t = tuple(user_numbers.split())
    t = tuple(map(int, strings_t))
    print(hash(t))