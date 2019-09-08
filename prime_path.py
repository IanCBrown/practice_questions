
def prime_path(start, finish):
    previous = start
    path = []
    changes = 0
    for i in range(start, finish + 1):
        if is_prime(i) and diff_of_one(previous, i):
            path.append(i)
            previous = i
            changes += 1
            print(changes)
            # i_diff_list = list(i)
    print(path)
    return len(path)

def is_prime(n):
    for i in range(2, n):
        if (n % i == 0):
            return False
    return True

def diff_of_one(string1, string2):
    string1 = str(string1)
    string2 = str(string2)
    count_diffs = 0
    for a, b in zip(string1, string2):
        if a!=b:
            if count_diffs: return False
            count_diffs += 1
    return True


def main():
    num_of_cases = int(input())
    list_of_cases = []
    for i in range(num_of_cases):
        list_of_cases.append([int(i) for i in input().split()])
    
    for case in list_of_cases:
        print(prime_path(case[0], case[1]))

    print(diff_of_one(1033, 1373))
    print(list_of_cases)

if __name__ == "__main__":
    main()