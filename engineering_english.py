import sys


def main():
    line = []
    line = input().split()

    line = [s.lower() for s in line]
    line = [s.strip() for s in line]

    count = {}
    ret_list = [] 

    while True: 
        for word in line:
            if word in count: 
                ret_list.append(".")
            else:
                ret_list.append(word)
                count[word] = 1
        try:    
            new = input().split()
            new = [s.lower() for s in new]
            new = [s.strip() for s in new]
        except EOFError:
            break
        line = new
    print(*ret_list, sep=' ')



if __name__ == "__main__":
    main()