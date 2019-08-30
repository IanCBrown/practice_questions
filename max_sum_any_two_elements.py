def get_max_sum(arr): 
    first_sum = max(arr)
    new_arr = [i for i in arr if i != first_sum]
    second_sum = max(new_arr)
    return [first_sum, second_sum]


def main():
    test_list = [3,7,4,6,5]

    print(get_max_sum(test_list))

if __name__ == "__main__":
    main()