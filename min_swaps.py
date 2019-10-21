# Complete the minimumSwaps function below.
# naive 
def minimumSwaps(arr):
    sample = sorted(arr)
    swaps = 0 
    i = 0
    while i < len(arr):
        if arr[i] != sample[i]:
            swap_target = sample[i]
            swap_location = arr.index(swap_target)
            temp = arr[i]
            arr[i] = arr[swap_location]
            arr[swap_location] = temp
            swaps += 1
        i += 1
    return swaps


def minimumSwapsDictionary(arr):
    positions = {}
    for i in range(len(arr)):
        positions[arr[i]] = i 
    swaps = 0 
    i = 0
    while i < len(arr):
        if arr[i] != i + 1:
            temp = arr[i]
            arr[i] = i + 1
            arr[positions[i + 1]] = temp
            
            # temp = positions[arr[i]]
            positions[temp] = positions[i + 1]
            # positions[i + 1] = temp
            swaps += 1
        i += 1
    return swaps