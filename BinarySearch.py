"""binary search"""

#docstring
def binary_search(array, target):
    """binary search"""
    _min = 0
    _max = len(array) - 1

    while _min <= _max:
        guess = int((_max + _min) / 2)
        if array[guess] == target:
            return array[guess]
        elif array[guess] < target:
            _min = guess + 1
        else:
            _max = guess - 1
    return -1

PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53,
          59, 61, 67, 71, 73, 79, 83, 89, 97]
TARGET = 97

print(binary_search(PRIMES, TARGET))
