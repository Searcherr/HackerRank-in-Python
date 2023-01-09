if __name__ == '__main__':
    N = int(input('Enter the number of commands: '))
    list = []
    for i in range(N):
        user_command = input(f"Command number {i+1}: ")
        list.append(user_command)

    splited_list = []
    list_of_commands = ('insert',
                        'print',
                        'remove',
                        'append',
                        'sort',
                        'pop',
                        'reverse')
    
    def to_split_list(user_list):
        for frase in user_list:
            checking_comand = frase.split()
            if checking_comand[0] in list_of_commands:
                splited_list.append(frase.split())
        return splited_list
    
    user_splited_list = to_split_list(list)
    
    result_list = []
    for command in user_splited_list:
        if (command[0] == 'insert') and (len(command) == 3):
            result_list.insert(int(command[1]), int(command[2]))
        if (command[0] == 'print') and (len(command) == 1):
            print(result_list)
        if (command[0] == 'remove') and (len(command) == 2):
            result_list.remove(int(command[1]))
        if (command[0] == 'append') and (len(command) == 2):
            result_list.append(int(command[1]))
        if (command[0] == 'sort') and (len(command) == 1):
            result_list.sort()
        if (command[0] == 'pop') and (len(command) == 1):
            result_list.pop()
        if (command[0] == 'reverse') and (len(command) == 1):
            result_list.reverse()
