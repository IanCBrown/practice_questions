
def two_sum_set(arr, target):
    saved = set()
    for i in range(len(arr)):
        if (target - arr[i]) in saved:
            return True
        else:
            saved.add(arr[i])
    return False


def two_sum_set_ret(arr, target):
    saved = set()
    for i in range(len(arr)):
        if (target - arr[i]) in saved:
            return (arr[i], target - arr[i])
        else:
            saved.add(arr[i])
    return False


if __name__ == "__main__":
    test_arr = [2,4,5,9,1]
    target = int(input())
    print(two_sum_set(test_arr, target))
    print(two_sum_set_ret(test_arr, target))
