import sys

# original problem 
# https://open.kattis.com/problems/t9spelling

new_map = {
    'a' : '2',
    'b' : '22',
    'c' : '222', 
    'd' : '3',
    'e' : '33',
    'f' : '333', 
    'g' : '4', 
    'h' : '44', 
    'i' : '444', 
    'j' : '5', 
    'k' : '55', 
    'l' : '555', 
    'm' : '6', 
    'n' : '66', 
    'o' : '666', 
    'p' : '7',
    'q' : '77',
    'r' : '777',
    's' : '7777',
    't' : '8',
    'u' : '88', 
    'v' : '888',
    'w' : '9',
    'x' : '99',
    'y' : '999',
    'z' : '9999', 
    ' ' : '0'}

def translation(string):
    ret_string = [new_map[string[0]]]
    previous = new_map[string[0]]
    for i in range(1, len(string)):
        char = new_map[string[i]]
        if previous[0] == char[0]:
            ret_string.append(' ')
        ret_string.append(char)
        previous = char
    return ''.join(ret_string)


def main():
    num_of_cases = int(input())
    list_of_cases = []
    for i in range(num_of_cases):
        list_of_cases.append(input())
    case_num = 1
    for case in list_of_cases:
        print("Case #" + str(case_num) + ": " + translation(case))
        case_num += 1
    

if __name__ == "__main__":
    main()