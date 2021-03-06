#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the twoStrings function below.
def twoStrings(s1, s2):
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    _s1 = list(s1)
    _s2 = list(s2)

    for char in alphabet:
        if _s1.__contains__(char) and _s2.__contains__(char):
            return "YES"
        
    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()

