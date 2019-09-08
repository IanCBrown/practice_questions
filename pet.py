import sys

def main():
    curr_max = [0, float("-inf")]
    line_num = 1 

    for line in sys.stdin.readlines():
        temp = sum([int(x) for x in line.split()]) 

        if temp > curr_max[1]:
            curr_max[0] = line_num
            curr_max[1] = temp
        line_num += 1

    print(*curr_max, sep=' ')




if __name__ == "__main__": 
    main()