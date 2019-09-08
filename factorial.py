
def factorial(a):
    if a == 0:
        return 1
    else:
        a = factorial(a - 1)
        return a

def factorial_itr(a):
    for i in range(a, -1):
        a *= (a - 1) 
    return a


print(factorial_itr(5))
