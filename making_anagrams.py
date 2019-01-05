#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    letter_count = {alphabet[i]: 0 for i in range(len(alphabet))}

    for char in a:
        letter_count[char]+= 1
    for char in b:
        letter_count[char]-= 1
    
    changes = 0 
    for letter in letter_count:
        changes += abs(letter_count[letter])
    
    return changes

    
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()

