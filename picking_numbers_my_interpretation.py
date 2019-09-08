# my interpretation of 
# https://www.hackerrank.com/challenges/picking-numbers/problem

def pickingNumbers(a):
    ret = []
    for num in a:
        temp = [] 
        for i in range(len(a)):
            if abs(num - a[i]) <= 1:
                temp.append(a[i])
        print(temp)
        if abs(max(temp) - min(temp)) <= 1:
            ret.append(temp)
    
    l = 0 
    for arr in ret:
        if l < len(arr):
            l = len(arr)
    print(ret) 
    return l
