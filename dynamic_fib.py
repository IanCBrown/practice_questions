
saved = {}
def fib_dp(num):
    num = int(num)
    result = 0

    if num == 1 or num == 0:
        return 1
    else:
        if num in saved:
            return saved[num]
        else:
            result = fib_dp(num - 1) + fib_dp(num - 2)
            saved[num] = result 
    return result



if __name__ == "__main__":
    num = input("Enter a number: ")
    print(fib_dp(num))