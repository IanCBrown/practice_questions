import sys


def add_until_odd(n):
    count = 0 
    # count cannot surpass 1000 
    while count < 1000:
        # += n with its reverse 
        n += int(str(n)[::-1])
        count += 1
        if contains_all_even_digits(n):
            print(str(count) + " " + str(n))
        
    
def contains_all_even_digits(n):
    l = [int(x) for x in str(n)]
    retVal = True
    for digit in l:
        if digit % 2 != 0:
            retVal = False
    return retVal


for line in sys.stdin:
    n = int(line)
    

add_until_odd(n)