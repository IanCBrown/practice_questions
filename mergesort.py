
def mergesort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        mergesort(L)
        mergesort(R)
        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        
        # remaining values 
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
	

def main():
    arr1 = [2,9, 3, 1, 3, 6, 5, 20, 4, 55]
    arr2 = [2,9, 3, 1, 3, 6, 5, 20, 4, 55]
    print(arr1)
    mergesort(arr1)
    print(arr1)
    

if __name__ == "__main__":
	main()
