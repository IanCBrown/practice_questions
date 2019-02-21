import sys 

def main():
    line = sys.stdin.readline().split()

    x = int(line[0])
    y = int(line[1])
    z = int(line[2]) 

    # division 
    if (x / y) == z:
        print(str(x) + "/" + str(y) + "=" + str(z))
    elif (y / z) == x:
        print(str(x) + "=" + str(y) + "/" + str(z))
    # multiplication 
    elif (x * y) == z:
        print(str(x) + "*" + str(y) + "=" + str(z))
    elif (y * z) == x:
        print(str(x) + "=" + str(y) + "*" + str(z))
    # subtraction 
    elif x - y == z:
        print(str(x) + "-" + str(y) + "=" + str(z))
    elif y - z == x:
        print(str(x) + "=" + str(y) + "-" + str(z))
    # addition 
    elif x + y == z:
        print(str(x) + "+" + str(y) + "=" + str(z))
    elif y + z == x:
        print(str(x) + "=" + str(y) + "+" + str(z)) 



if __name__ == "__main__":
    main()