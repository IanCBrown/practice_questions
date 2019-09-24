

def factorial(a):
    if a == 0:
        return 1
    else:
        return a * factorial(a - 1) 
    

def last_digit(a):
    return str(a)[-1]



def main():
    num_cases = int(input())
    while num_cases > 0:
        f = factorial(int(input()))
        print(last_digit(f))
        num_cases -= 1

if __name__ == "__main__":
    main()