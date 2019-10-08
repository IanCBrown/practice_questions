
import sys

vowels = ['a','e','i','o','u']

def reverse_vowels(string):
    string = list(string)
    left_ptr = 0
    right_ptr = len(string) - 1 
    temp = ""
    while left_ptr < right_ptr:
        if string[left_ptr].lower() not in vowels:
            left_ptr += 1
        elif string[right_ptr].lower() not in vowels:
            right_ptr -= 1
        else:
            temp = string[right_ptr]
            string[right_ptr] = string[left_ptr]
            string[left_ptr] = temp 
            right_ptr -= 1
            left_ptr += 1
    return "".join(string)

if __name__=='__main__':
    test_string = input("Input a string: ")
    print(reverse_vowels(test_string))
