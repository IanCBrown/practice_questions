# 1,2,3,4,5,6,7,7,8,8,9
# k = 3
# k_copy = 5


# breaks in some cases 
# fix later
def kmax(arr, k):
    
    prev = arr[0]
    for i in range(1, len(arr)):
        if prev == arr[i]:
            k += 1
        prev = arr[i]
    
    return arr[len(arr) - k]

# works for all 
# uses O(N) space
def kmax_set(arr, k):
    arr.sort()
    
    ret = [] 
    prev = arr[0]
    ret.append(prev)
    for i in range(len(arr)):
        if prev != arr[i]:
            ret.append(arr[i])
        prev = arr[i]
    print(ret)
    print(ret[len(ret) - k])

    


l = [1,2,3,4,5,6,7,7,8,8,9]
l2 = [3,7,3,3,1,9,1,1,1,5]
print(list(sorted(l2)))
k = 3

print(kmax(l2,k))
print(kmax_set(l2, k))