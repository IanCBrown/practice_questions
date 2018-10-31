
def highest_tidy_number(n):
    num = int(n)
    for i in range(num,0, -1):
        a = list(map(int, list(str(i))))
        if is_tidy(a):
            return i 
    return -1

def is_tidy(int_to_list):
    j = 0 
    for i in range(1, len(int_to_list)):
        if int_to_list[j] > int_to_list[i]:
            return False
        j += 1
    return True


def main():
    num_of_cases = int(input())
    for i in range(num_of_cases):
        case = input()
        print("Case #{0}: {1}".format(i + 1, str(highest_tidy_number(case))))
    


if __name__ == "__main__":
    main()