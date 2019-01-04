#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSwaps function below.
def countSwaps(a):
    num_swaps = 0 
    for i in range(len(a)):
        for j in range(len(a) - 1):
            if a[j] > a[j + 1]:
                #swap
                swap(a, j, j + 1)
                num_swaps += 1
    
    print("Array is sorted in %d swaps." % num_swaps)
    print("First Element: %d" % a[0])
    print("Last Element: %d " % a[-1])


def swap(a, v1, v2):
    temp = a[v1]
    a[v1] = a[v2]
    a[v2] = temp

if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
