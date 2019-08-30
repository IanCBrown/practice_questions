arr = [0,1,0,1,0,0,1,1,1,0]

def move_zeros(arr):
    count = 0 

    for i in range(len(arr)):
        if arr[i] == 0:
            arr[count] = arr[i]
            count += 1

    while count < len(arr):
        arr[count] = 1
        count += 1 
    return arr 


move_zeros(arr)
print(arr)
    

