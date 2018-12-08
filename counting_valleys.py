#!/bin/python3

import math
import os
import random
import re
import sys

# Hackerrank 
# https://www.hackerrank.com/challenges/counting-valleys/problem

# Complete the countingValleys function below.
def countingValleys(n, s):
    running_sum = 0 
    valley_count = 0
    for feature in s:
        if feature == 'D':
            running_sum -= 1
        elif feature == 'U':
            running_sum += 1
        if running_sum == 0 and feature == 'U':
            valley_count += 1
    return valley_count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
