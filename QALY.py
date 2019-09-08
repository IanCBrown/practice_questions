

def QALY(period_dict):
    total = 0 
    for k, v in period_dict.items(): 
        total += (k * v)
    return total

def main():
    num_periods = int(input())
    periods = {}
    line = []

    while num_periods > 0: 
        line.append(input().split())
        num_periods -= 1
    
    for p in line:
        periods[float(p[0])] = float(p[1])
    print("%.3f" % QALY(periods))


if __name__ == "__main__":
    main()