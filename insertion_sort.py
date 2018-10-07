def insertion_sort(arr):
    for i in range(len(arr)):
        j = i 
        while j > 0:
            if arr[j] <  arr[j - 1]:
                temp = arr[j - 1]
                arr[j - 1] = arr[j]
                arr[j] = temp
                j -= 1
            else:
                j -= 1
                break
  
if __name__ == "__main__":
    test_arr = [23, 3, 4, 64, 1, 0, 8, 6, 9, 2, 12, 43]
    insertion_sort(test_arr)
    print(test_arr)
