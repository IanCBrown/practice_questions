

def exponent(a, b):
    total = 1
    for i in range(b):
        total = multiply(total, a)
    return total 


def multiply(a, b):
    total = 0
    for i in range(b):
        total += a
    return total 


print(multiply(5,3))
print(exponent(5, 3))