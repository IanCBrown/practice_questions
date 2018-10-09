import sys

def minimal_n(L, D, X):
    min = D
    for i in range(D + 1, L - 1, -1):
        if (sum_of_digits(i) == X) and i < min:
            min = i 
    return min

def maximal_m(L, D, X): 
    max = 0
    for i in range(L, D + 1):
        if (sum_of_digits(i) == X) and i > max:
            max = i
    return max

def sum_of_digits(num):
    sum = 0 
    while num > 0:
        # gets digit 
        sum += num % 10
        # reduce order of magnitude and repeat 
        num = num // 10
    return sum


if __name__ == "__main__":
    nums = sys.stdin.readlines()
    L = int(nums[0])
    D = int(nums[1])
    X = int(nums[2])
    
    print(minimal_n(L, D, X))
    print(maximal_m(L, D, X))


