

def find_subarray_slow(s, arr):
    total = 0 
    j = 0
    l = []
    for i in range(len(arr)):
        total += arr[i]
        l.append(arr[i])
        for j in range(i + 1, len(arr)):
            if total == s:
                return l
            total += arr[j] 
            l.append(arr[j])
        total = 0
        l = []
    return []


def subarray_sum(s, arr):
    total = arr[0] 
    l = []
    l.append(arr[0])
    return []



test = [5,4,3,21,3,4,5,6,4,6]
s = 27
print(find_subarray_slow(s,test))
#print(subarray_sum(s,test))