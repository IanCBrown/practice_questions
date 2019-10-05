import sys

# https://math.stackexchange.com/questions/876352/how-can-i-calculate-the-total-number-of-possible-anagrams-for-a-set-of-letters/876356
# Useful formula 


# precalculate factorials to save time 
factorials = {}
def factorial_helper():
    for i in range(101):
        factorial(i)
def factorial(n):
    if n == 0:
        factorials[n] = 1
        return 1
    else:
        value = n * factorial(n - 1)
        factorials[n] = value
        return value


factorial_helper()
for line in sys.stdin:
    line = line.strip()
    counts = {}
    for char in line:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1

    ret_value = factorials[len(line)]
    for char, count in counts.items():
        ret_value //= factorials[count]
    print(ret_value)