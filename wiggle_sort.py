
# "wiggle sort" in linear and nlogn time 
def wiggle_nlogn(arr):
    working = sorted(arr)
    for i in range(0, len(working) - 2, 2):
        swap(working, i, i + 1)
    return working


def wiggle_linear(arr):
    working = arr
    for i in range(0, len(working) - 2, 2):
        if i > 0 and working[i] < working[i - 1]:
            swap(working, i, i - 1)
        if working[i] < working[i + 1]:
            swap(working, i, i + 1)
    return working

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def main():
    arr = [10, 90, 49, 2, 1, 5, 23]
    print(wiggle_nlogn(arr))
    print(wiggle_linear(arr))



if __name__ == "__main__":
    main()