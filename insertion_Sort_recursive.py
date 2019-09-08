def recursive_insertion_sort(l, n):
    if n > 1:
        recursive_insertion_sort(l, n - 1)
    else:
        key = l[n]
        i = n - 1
        while i > 0 and l[i] > key:
            l[i + 1] = l[i]
            i -= 1
        l[i + 1] = key 
    return l


def main():
    l = [1, 3, 2, 6, 7, 4, 65, 7]
    print(recursive_insertion_sort(l, 8))


if __name__ == "__main__":
    main()