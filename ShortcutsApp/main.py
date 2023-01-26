class Template:
    def __init__(self, message, shortcut, path_to_file):
        self.message = message
        self.shortcut = shortcut
        self.path_to_file = path_to_file

    def __str__(self):
        return f"{self.message}, {self.shortcut}, {self.path_to_file}"

    def read_file(self, path_to_file):
        with open(self.path_to_file) as file:
            lines = [line.rstrip() for line in file]
        return lines

    def make_shortcut(self):
        pass

if __name__ == '__main__':
    user_file = '/Users/dmytror/Documents/test_files.Text1.tct'
    user_template = Template()


    print(user_template.__dict__)



# bubble_sort.py
def bubble_sort(array):
    for i in range(len(array)):
        for j in range(len(array) - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array