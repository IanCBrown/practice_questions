#!/bin/python3

from collections import deque
import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
    if d == 0:
        return a
    a = a[1:] + [a[0]]
    return rotLeft(a, d - 1)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

