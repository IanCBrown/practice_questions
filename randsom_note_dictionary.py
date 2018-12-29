#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    m_dict = {}
    note_dict = {}
    for word in magazine:
        if word in m_dict:
            m_dict[word] += 1
        else:
            m_dict[word] = 1
    
    for word in note:
        if word in note_dict:
            note_dict[word] += 1
        else:
            note_dict[word] = 1
    
    try:
        for word in note_dict:
            if m_dict[word] >= note_dict[word]:
                    continue
            else:
                print("No")
                return
    except KeyError:
        print("No")
        return

    print("Yes")
    return 

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)

