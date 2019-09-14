
def add(arr, b):
    # a, b
    # number a is represented as an array. 
    # add number b to it 
    a = "".join([str(x) for x in arr])
    a = int(a)
    a += b
    return list(str(a))


def add_one(arr):
    # add one to the array representing a number [1,2,3,4] + 1 = [1,2,3,5]
    # [1,9,9] --> [2,0,0]
    ret = [0] * len(arr)
    carry = 1

    for i in range(len(arr) - 1, -1, -1):
        ret[i] = arr[i] + carry
        if ret[i] <= 9:
            carry = 0
        else: 
            ret[i] = 0
            carry = 1
    # if carry still equals one, increase size 
    if carry == 1:
        ret = [0] * (len(ret) + 1)
        ret[0] = 1

    return ret
        

print(add([1,2,3,4], 6))
print(add([9,9,9], 1))

print(add_one([1,2,3,4]))
print(add_one([1,9,9]))
print(add_one([9,9,9]))