
def subarrays_sum(arr):
    # dynamic programming 
    # reduces complexity from n^3 to n^2
    result = 0 
    for i in range(len(arr)):
        sum = 0
        for j in range(i,len(arr)):
            sum += arr[j]
            result += sum 
    return result


def main():
    test = [1, 3, 7]
    print(subarrays_sum(test))


if __name__ == "__main__":
    main()