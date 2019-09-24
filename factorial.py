
def factorial(a):
    if a == 0:
        return 1
    else:
        return a * factorial(a - 1)

def factorial_itr(a):
    for i in range(1, a):
        a *= i 
    return a


print("iterative: " + str(factorial_itr(5)))
print("recursive: " + str(factorial(5)))
