import sys


allotment = int(input())
num_months = int(input())
usage = [int(x) for x in sys.stdin.readlines()]

carry = 0
for use in usage:
    carry += allotment
    carry -= use

# for month N + 1 add another allotment 
print(carry + allotment)