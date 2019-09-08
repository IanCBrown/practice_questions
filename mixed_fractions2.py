
# original problem 
# https://open.kattis.com/problems/mixedfractions


def main():
    while True:
        n, m = map(int, input().split())
        if n == m == 0:
            break

        base = n // m 

        rem = n % m 
        print(base, rem, '/', m)


if __name__ == '__main__':
    main()