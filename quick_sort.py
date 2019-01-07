import random


def quick_sort(l, low, high):
    if low < high:
        q = partition(l, low, high)
        quick_sort(l, low, q - 1)
        quick_sort(l, q + 1, high)

def partition(l, low, high):
    x = l[high] 
    i = low - 1 

    # for j = p to r - 1
    for j in range(low, high):
        if l[j] <= x:
            i += 1
            swap(l, i, j)
    swap(l, i+1, high)
    return i + 1

def swap(l, a, b):
    temp = l[a]
    l[a] = l[b]
    l[b] = temp 
    return l

def get_random_list(max, length):
    return [random.randrange(0, max) for _ in range(0, length)]

def main():
    test_list = get_random_list(10, 100)
    print(test_list)
    quick_sort(test_list, 0, 99)
    print(test_list)



if __name__ == "__main__":
    main()