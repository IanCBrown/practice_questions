#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    am_pm = s[len(s) - 2:]
    hour = ''

    if s[:2] == '12' and am_pm == 'PM':
        return s[:len(s) - 2]
    elif s[:2] == '12':
        hour = '00'
        return (str(hour) + s[2:len(s) - 2])
    elif am_pm == 'PM':
        hour = int(s[:2])
        hour += 12
        return (str(hour) + s[2:len(s) - 2])
    else:
        return s[:len(s) - 2]


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()

