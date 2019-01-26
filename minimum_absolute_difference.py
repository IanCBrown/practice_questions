#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(arr):
    m = float("inf")

    arr.sort()
    j = 1
    for i in range(len(arr) - 1):
        temp = abs(arr[i] - arr[j])
        m = min(m, temp)
        j += 1
    return m 


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

