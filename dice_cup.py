
def main():
    line = input().split()
    x = int(line[0])
    y = int(line[1])

    results = {}
    
    for i in range(1, x + 1):
        for j in range(1, y + 1):
            temp = i + j
            if temp in results:
                results[temp] += 1
            else:
                results[temp] = 1

    retlist = [] 
    max_value = max(results.values())
    [retlist.append(key) for key in results if results[key] == max_value]
    retlist.sort()
    print(*retlist, sep='\n')

if __name__ == "__main__":
    main()