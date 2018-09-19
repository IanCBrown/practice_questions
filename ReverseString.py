#!/usr/bin/env python

import sys

string = input("Input a string to be reversed: \n")
if len(string) == 0 or len(string) == 1:
    print("{} is not long enough to be reversed".format(string))
    sys.exit()

print(''.join(reversed(string)))
