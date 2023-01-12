if __name__ == '__main__':

    # Returns True if  has any alphanumeric characters. Otherwise - False
    def has_alphanumeric(input_string):
        for char in input_string:
            if char.isalnum():
                return True
        return False


    # Returns True if  has any alphabetical characters. Otherwise - False
    def has_alphabetical(input_string):
        for char in input_string:
            if char.isalpha():
                return True
        return False

    # Returns True if has any digits. Otherwise - False
    def has_digits(input_string):
        for char in input_string:
            if char.isdigit():
                return True
        return False


    # Returns True if  has any lowercase characters. Otherwise - False
    def has_lowercase(input_string):
        for char in input_string:
            if char.islower():
                return True
        return False


    # Returns True if  has any uppercase characters. Otherwise - False
    def has_uppercase(input_string):
        for char in input_string:
            if char.isupper():
                return True
        return False

    s = 'qA2'
    # s = input()
    print(has_alphanumeric(s))
    print(has_alphabetical(s))
    print(has_digits(s))
    print(has_lowercase(s))
    print(has_uppercase(s))
