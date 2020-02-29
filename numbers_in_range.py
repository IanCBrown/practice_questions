# leetcode

def find_digit(l, r, q):
    count = 0 
    
    for i in range(l, r + 1):
        # print(i)
        I = to_set(i)
        Q = to_set(i * q)
        if len(I.intersection(Q)) == 0:
            count += 1
    return count
        


def to_set(num):
    l = str(num)
    ret = [int(i) for i in l]
    return set(ret)

l = 10
r = 12
q = 2

# l, r, q
print(find_digit(10,12,2))
print(find_digit(5,15,2))