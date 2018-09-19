def power_of_2_iterative(n):
    temp = 1
    while n > 0:
        temp = n * 2
        n = n - 1
    return temp
    

if __name__ == '__main__':
    print(power_of_2_iterative(4))
