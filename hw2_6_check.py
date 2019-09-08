def rec(n):
    if n <= 1:
        return n
    else:
        return (5 * rec(n - 1) - 6 * rec(n - 2))



if __name__ == "__main__":
    print(rec(4))
