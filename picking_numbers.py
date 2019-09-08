#!/bin/python3

import math
import os
import random
import re
import sys

# https://www.hackerrank.com/challenges/picking-numbers/problem
def pickingNumbers(a):
    num = 0 
    freq = [0] * 100

    for i in range(len(a)):
        freq[a[i]] += 1    
    
    for i in range(1, 100):
        num = max(num, freq[i] + freq[i - 1])
    return num 


