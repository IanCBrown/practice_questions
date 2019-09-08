

def get_adjacent_elements(arr): 
    ret_list = set()
    for i in range(0, len(arr) - 2, 2):
        ret_list.add(arr[i]) 
    return ret_list 

def main():
    test_list = [3,7,4,6,5]

    print(get_adjacent_elements(test_list))

if __name__ == "__main__":
    main()