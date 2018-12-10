#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
# n^2 Solution 
def rotLeft(a, d):
    ret_val = []
    for i in range(d):
        ret_val = rotate(a)
    return ret_val
    

def rotate(a):
    save_front = a[0] 
    for i in range(0, len(a) - 1):
        a[i] = a[i + 1]
    a[-1] = save_front
    return a

if __name__ == '__main__':

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)



