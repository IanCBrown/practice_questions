


def sum_of_n_recursive(n):
    if n == 0:
        return n 
    return (n - 1) + sum_of_n_recursive(n - 1)

def sum_of_n_iterative(n):
    total = 0
    for i in range(n):
        total += i
    return total



def main():
    n = int(input("Enter a number n: "))
    print("Recursive: " + str(sum_of_n_recursive(n)))
    print("Iterative: " + str(sum_of_n_iterative(n)))


if __name__ == "__main__":
    main()