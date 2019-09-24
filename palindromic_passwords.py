import sys

def is_palindrome(number):
    number = list(number)
    if len(number) != 6:
        return False
    return number[0] == number[len(number) - 1] and number[1] == number[len(number) - 2] and number[2] == number[len(number) - 3]

num_cases = int(input())

while num_cases > 0:
    curr_num = int(input())

    result = -1
    diff = 0 
    while (result == -1):
        if is_palindrome(str(curr_num - diff)):
            result = curr_num - diff 
        elif is_palindrome(str(curr_num + diff)):
            result = curr_num + diff  
        diff += 1     
    print(result)  
    num_cases -= 1