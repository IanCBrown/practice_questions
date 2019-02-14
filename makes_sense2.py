import sys 


def main(): 
    num = int(input())
    line = sys.stdin.readline().split()
    
    current = 0
    mumble_count = 0  
    ok = True

    for i in range(num):
        current += 1
        if line[i] == "mumble":
            continue
        else:
            if int(line[i]) != current:
                ok = False

    if ok:
        print("makes sense")
    else: 
        print("something is fishy")


if __name__ == "__main__":
    main()