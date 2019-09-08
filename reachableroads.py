

def union(a, b, graph):
    # union with path compression 
    aParent = find(a, graph)
    bParent = find(b, graph) 
    if aParent > bParent: 
        graph[aParent] = bParent
    else:
        graph[bParent] = aParent

def find(index, graph): 
    if graph[index] == index:
        return index
    graph[index] = find(graph[index], graph)
    return graph[index]



def main():
    graph = [] 
    # number of test cases
    # number of cities
    # number of roads
    # descript of road connections 

    num_cases = int(input())

    # for each test case 
    for i in range(num_cases):
        cities = int(input()) 
        roads = int(input())

        graph = [0]*cities 
        for j in range(cities):
            graph[j] = j 
        
        for k in range(roads):
            line = input().split()
            a = int(line[0]) 
            b = int(line[1]) 

        uniqueParents = set()
        for l in range(cities):
            uniqueParents.add(find(l, graph))

        print(uniqueParents)
        print(len(uniqueParents) - 1)


if __name__ == "__main__":
    main()