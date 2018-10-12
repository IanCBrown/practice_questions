def checkPalindrome(inputString):
    # iterate from left to right, store items in list 
    # iterate from right to left, store items in list
    # compare lists 
    left_to_right = list(inputString)
    right_to_left = list(reversed(inputString))
    print(left_to_right)
    print(right_to_left)
    
    if left_to_right == right_to_left:
        return True
    else:
        return False 

def main():
    i_string = input()
    print(checkPalindrome(i_string))

if __name__ == "__main__":
    main()