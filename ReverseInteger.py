#!/usr/bin/env python

import sys

number = str(input("Enter an integer to be reversed \n"))
if len(number) == 0 or len(number) == 1:
    print("{} is not long enough to be reversed".format(number))
    sys.exit()

print(''.join(reversed(number)))
