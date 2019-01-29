

def main():
    total = 0 
    num_periods = int(input())
    while num_periods:
        line = input().split()
        q, p = float(line[0]), float(line[1])
        total += q * p 
        num_periods -= 1
    print(total)

if __name__ == "__main__":
    main()