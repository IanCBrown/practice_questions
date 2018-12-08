#!/bin/python3

import math
import os
import random
import re
import sys

# Hackerrank 
# https://www.hackerrank.com/challenges/compare-the-triplets/problem

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    ret_ar = [0, 0]
    
    for i in range(len(a)):
        if a[i] == b[i]: 
            continue
        if a[i] > b[i]:
            ret_ar[0] += 1
        else: 
            ret_ar[1] += 1
    return ret_ar
        
     

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
