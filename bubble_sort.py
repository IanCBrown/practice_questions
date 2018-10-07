def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[j] > arr[i]:
                temp = arr[j]
                arr[j] = arr[i]
                arr[i] = temp

if __name__ == "__main__":
    test_arr = [23, 3, 4, 64, 1, 0, 8, 6, 9, 2, 12, 43]
    bubble_sort(test_arr)
    print(test_arr)
