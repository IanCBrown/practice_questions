#!/bin/python3

import math
import os
import random
import re
import sys



# Complete the maxDifferenceOddEven function below.
def maxDifferenceOddEven(a):
    evens = [] 
    odds = []
    max_found = -1
    for i in range(len(a)):
        if a[i] % 2 == 0:
            evens.append(a[i])
        #elif i % 2 != 0:
        else:
            odds.append(a[i]) 
    
    # clean up evens
    for j in evens:
        if len(odds) != 0 and j < max(odds):
            evens.remove(j)
    

    print(evens)
    print(odds)

    for i in range(len(odds)):
        if len(evens) != 0 and len(odds) != 0:
            temp = max(evens) - min(odds)
            if temp > max_found:
                max_found = temp
            else:
                evens.remove(max(evens))
                odds.remove(max(odds))
    return max_found

    


if __name__ == '__main__':