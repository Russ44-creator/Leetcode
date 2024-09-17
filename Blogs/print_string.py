from curses.ascii import isdigit


string = "abc3de2fg3"

# [3, 2]

def print_string(string):
    index = len(string) - 1
    string_temp = ""
    
    if isdigit(string[index]):
        for i in range(int(string[index])):
            print_string(string[:index])
            print(string_temp[::-1])
    else:
        while index >= 0 and not isdigit(string[index]):
            string_temp += string[index]
            index -= 1
            # print(string_temp)
        if index >= 0:
            print_string(string[:index + 1])
        print(string_temp[::-1])

print_string(string)
