import math

# think of problem as a binary tree
# the height of said tree is log(n) 
# if each leaf produces a new printer each day 
# the tree will always be full


def main():
    n = int(input())
    
    print(math.ceil(math.log(n, 2) + 1))


if __name__ == "__main__":
    main()
