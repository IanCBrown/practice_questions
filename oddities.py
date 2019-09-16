

def odd(num):
    if num % 2 == 0:
        return "%d is even" % num
    else:
        return "%d is odd" % num 



def main():
    num_cases = int(input())
    while num_cases > 0:
        case = int(input())
        print(odd(case))
        num_cases -= 1


if __name__ == "__main__":
    main()