# 1,2,3,4,5,6,7,7,8,8,9
# k = 3
# k_copy = 5



def kmax(arr, k):
    
    prev = arr[0]
    for i in range(1, len(arr)):
        if prev == arr[i]:
            k += 1
        prev = arr[i]
    
    return arr[len(arr) - k]


l = [1,2,3,4,5,6,7,7,8,8,9]
k = 3

print(kmax(l,k))