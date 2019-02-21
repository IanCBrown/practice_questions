import sys 
import math

def main():

    line = sys.stdin.readline() 
    line = line.split()


    p = l = r = m = 0 

    while len(line) > 0:
        m = int(line[0])
        p = int(line[1])
        l = int(line[2])
        e = int(line[3])
        r = int(line[4])
        s = int(line[5])
        n = int(line[6])

        while n > 0: 
            new_l = m * e
            new_p = l // r
            new_m = p // s
            
            l = new_l
            p = new_p
            m = new_m            

            n -= 1 

        print(new_m)
        line = sys.stdin.readline().split() 







if __name__ == "__main__":
    main()