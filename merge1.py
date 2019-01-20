def merge(arr1, arr2):
    """merge two sorted arrays"""
    n1 = len(arr1)
    n2 = len(arr2)
    ret_arr = []

    i = 0 
    j = 0 

    while i < n1 and j < n2:
        if arr1[i] < arr2[j]:
            ret_arr.append(arr1[i])
            i += 1
        else:
            ret_arr.append(arr2[j])
            j += 1 
    
    while i < n1:
        ret_arr.append(arr1[i])
        i += 1
    
    while j < n2:
        ret_arr.append(arr2[j])
        j += 1
    
    return ret_arr


def main():
    arr1 = [1,3,5,7]
    arr2 = [0,2,4,6]

    print(merge(arr1, arr2))


if __name__ == "__main__": 
    main()