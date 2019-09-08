#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    base = ['#'] * n
    spaces = [' '] * n 
    out = []

    for i in range(1, n + 1):
        print(''.join(spaces[:n - i] + base[:i]))

    

if __name__ == '__main__':
    n = int(input())

    staircase(n)

