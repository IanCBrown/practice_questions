#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hackerrankInString function below.
def hackerrankInString(s):
    h = ['h','a','c','k','e','r','r','a','n','k']

    l = list(s)
    n = len(l)
    if n < len(h):
        return "NO"
    j = 0 
    for i in range(n):
        if j < len(h) and l[i] == h[j]:
            j += 1
    if j == len(h):
        return "YES"
    else:
        return "NO"
    

if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = hackerrankInString(s)

        print(result)

