

def kmin(arr, k):
    arr.sort()

    return arr[k - 1]


def kmax(arr, k):
    arr.sort()

    return arr[len(arr) - k]


def kmin_no_duplicates(arr, k):
    if k < 1:
        return -1 

    arr.sort()

    j = 1
    k_count = 1
    for i in range(len(arr)):
        if arr[i] != arr[j]:
            k_count += 1
            if k_count == k:
                return arr[j]
        j += 1

    if k > k_count:
        return -1


def kmax_no_duplicates(arr, k):
    if k < 1:
        return -1

    arr.sort()

    j = len(arr) - 2
    k_count = 1

    for i in range(len(arr) - 1, 0, - 1):
        if arr[i] != arr[j]:
            k_count += 1
            if k_count == k:
                return arr[j]
        j += 1

    if k > k_count:
        return -1

    
def main():
    test = [0,0,1,1,3,4,5,5,6]
    k = 2

    print(kmin_no_duplicates(test, k))
    print(kmax_no_duplicates(test, k))

if __name__ == "__main__":
    main()
