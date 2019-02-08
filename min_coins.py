import sys


def min_coins(total):
    if total % 5 == 0: 
        return int(total / 5)
    elif (total % 5) == 3:
        return int((total / 5) + 1)
    elif (total % 5) == 4:
        return int((total / 5) + 2)
    else:
        return int((total / 5) + (total % 5))
    

total = int(input())


print(min_coins(total))
    
