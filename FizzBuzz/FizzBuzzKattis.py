import sys

def fizzbuzz(x, y, z):
    for i in range(1, z + 1):
        if i % x == 0 and i % y == 0:
            print("FizzBuzz")
        elif i % x == 0:
            print("Fizz")
        elif i % y == 0:
            print("Buzz")
        else:
            print(i)

if __name__ == "__main__":
    input = sys.stdin.readline().split()
    x = int(input[0])
    y = int(input[1])
    z = int(input[2])
    fizzbuzz(x, y, z)


