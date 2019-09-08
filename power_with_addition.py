

def power(a, b):
    if b == 0:
        return 1

    prev = a 
    total = a
    for i in range(b - 1):
        for j in range(a - 1):
            total += a
    prev = total 
    return total


print(power(5,3))
