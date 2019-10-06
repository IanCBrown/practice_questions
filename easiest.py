import sys


def sum_of_digits(number):
    n = list(str(number))
    n = [int(x) for x in n]
    val = 0
    for i in range(len(n)):
        val += n[i]
    return val


def find_p(number):
    p = 11 

    while True:
        if sum_of_digits(p * number) == sum_of_digits(number):
            return p
        p += 1


for num in sys.stdin:
    case = int(num.strip())
    if case == 0:
        break 
    print(find_p(case))
