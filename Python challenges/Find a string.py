def count_substring(string, sub_string):
    count = 0
    for i in range(len(string) - len(sub_string)+1):
        if string[i] == sub_string[0]:
            is_in = True
            for j in range(len(sub_string)):
                if string[i+j] != sub_string[j]:
                    is_in = False
            if is_in == True:
                count += 1
    return count


if __name__ == '__main__':
    string = input('Input your text: ').strip()
    sub_string = input('').strip()
    print(string, sub_string)

    count = count_substring(string, sub_string)
    print(count)