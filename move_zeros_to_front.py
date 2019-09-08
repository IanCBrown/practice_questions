
arr = [0,1,0,1,0,0,1,1,1,0]


def move_zeros(arr):
    zero_count = 0
    one_count = 0
    for i in range(len(arr)):
        if arr[i] == 0:
            zero_count += 1

    for i in range(len(arr)):
        if arr[i] == 0:
            one_count += 1

    print(zero_count)

    ret_arr = [0 for i in range(zero_count)]
    ret_arr += [1 for i in range(one_count)]
    return ret_arr



print(move_zeros(arr))