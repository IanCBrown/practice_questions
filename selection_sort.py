def selection_sort(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i + 1, len(arr)):
            if arr[j] <  arr[min]:
                min = j
        temp = arr[min]
        arr[min] = arr[i]
        arr[i] = temp
  
if __name__ == "__main__":
    test_arr = [23, 3, 4, 64, 1, 0, 8, 6, 9, 2, 12, 43]
    selection_sort(test_arr)
    print(test_arr)
