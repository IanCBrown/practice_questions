import sys 

def main():
    a = [int(x) for x in sys.stdin.readline().split()] 
    b = [int(x) for x in sys.stdin.readline().split()]
    c = [int(x) for x in sys.stdin.readline().split()]

    x_and_y = [sorted(list(l)) for l in zip(a, b, c)]
    xs = x_and_y[0]
    ys = x_and_y[1]

    new_x = 0
    new_y = 0
     # if two points are in the same line, look for diff in x and y 
    if xs[0] == xs[1]:
        new_x = xs[2]
    else:
        new_x = xs[0]
    
    if ys[0] == ys[1]:
        new_y = ys[2]
    else:
        new_y = ys[0]
    
    # str(rx) + " " + str(ry)
    return str(new_x) + " " + str(new_y)


if __name__ == "__main__":
    print(main())