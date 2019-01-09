#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumNumber function below.
def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    lower_req = 1
    upper_req = 1
    num_req = 1
    length_req = 6
    special_req = 1
    special_chars = "!@#$%^&*()-+"
    req_sum = 0  
    
    for c in password:
        if ord(c) >= 65 and ord(c) <= 90:
            lower_req = 0
        elif ord(c) >= 97 and ord(c) <= 122:
            upper_req = 0 
        elif c.isdigit():
            num_req = 0 
        elif c in special_chars:
            special_req = 0

    req_sum = lower_req + upper_req + num_req + special_req
    

    if n < length_req and req_sum > length_req - n:
        return req_sum 
    elif n < length_req:
        return length_req - n
    else: 
        return req_sum 
  

        


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()

