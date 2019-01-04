#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    j = 0 
    count = 0 

    for i in range(len(q) - 1):
        if q[i] - (i + 1) > 2:
            print("Too chaotic")
            return
    
    for i in range(len(q)):
        for j in range(len(q) - i - 1): 
            if q[j] > q[j + 1]:
                q[j],q[j + 1] = q[j + 1],q[j]
                count += 1
    print(count)

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
