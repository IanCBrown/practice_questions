#!/bin/python3

import os
import sys

#
# Complete the gradingStudents function below.
#
def gradingStudents(grades):
    fl = 0 
    for i in range(len(grades)):
        if grades[i] < 38:
            continue
        fl = grades[i] // 5
        fl *= 5
        if ((fl + 5) - grades[i]) < 3:
            grades[i] = (fl + 5)
    return grades

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grades = []

    for _ in range(n):
        grades_item = int(input())
        grades.append(grades_item)

    result = gradingStudents(grades)

    f.write('\n'.join(map(str, result)))
    f.write('\n')

    f.close()

