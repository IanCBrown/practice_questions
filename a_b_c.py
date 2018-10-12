import sys

# original problem 
# https://open.kattis.com/problems/abc
# solution using dictionaries 

def arrange(num_list, abc_order):
    return_string = ""
    num_list.sort()
    num_letter_pairs = {"A" : num_list[0], "B" : num_list[1], "C" : num_list[2]}

    for letter in abc_order:
        return_string += str(num_letter_pairs[letter]) + " "

    return return_string



def main():
    nums = input().split()
    nums = [int(i) for i in nums]
    abc_order = input()
    abc_order = list(abc_order)
    print(arrange(nums, abc_order))


if __name__ == "__main__":
    main()