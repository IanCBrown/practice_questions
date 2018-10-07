
def twosum(arr, t):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] + arr[j] == target:
                return True
            else:
                return False


if __name__ == "__main__":
    target = int(input())
    test_arr = [2, 4, 5, 9, 1]
    print(twosum(test_arr, target))
