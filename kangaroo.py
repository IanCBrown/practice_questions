#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    pos1 = x1 
    pos2 = x2 
    # 100000000 is the largest possible size of pos1 and pos2 
    while pos1 != pos2 and pos1 <= 100000000 and pos2 <= 100000000:
        pos1 += v1
        pos2 += v2 
        if pos1 == pos2:
            return 'YES'
    return 'NO'
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()

