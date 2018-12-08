#!/bin/python3
from collections import Counter
import math
import os
import random
import re
import sys

# Hackerrank 
# https://www.hackerrank.com/challenges/sock-merchant/problem


# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    num_of_pairs = 0 
    color_set = set() 
    for color in ar:
        color_set.add(color)
    
    counts = Counter(ar)
    for color in color_set:
        print(counts[color])
        if counts[color] > 1:
            num_of_pairs += counts[color] // 2
    return num_of_pairs



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
