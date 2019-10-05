import heapq 
from queue import PriorityQueue


def find_path(adj, num_of_nodes):
    visited = set()
    pq = []
    # tuple (weight, index)
    start = (-1, list(adj)[0])
    visited.add(start)
    pq.append(start)
    heapq.heapify(pq)

    while pq:
        curr = heapq.heappop(pq) 
        if curr[1] in adj:
            neighbors = adj[curr[1]]
        if curr[1] == num_of_nodes:
            return "{0:.4f}".format(curr[0] * -1)
        for index, weight in neighbors.items():
            new_neighbor = (-weight * curr[0], index)
            pq.append(new_neighbor)
            visited.add(new_neighbor)
    return 


def find_path_pq(adj, num_of_nodes):
    visited = set()
    pq = PriorityQueue()
    # tuple (weight, index)
    start = (-1, list(adj)[0])
    visited.add(start)
    pq.put(start)

    while pq:
        print(pq.queue)
        curr = pq.get() 
        if curr[1] in adj:
            neighbors = adj[curr[1]]
        if curr[1] == num_of_nodes:
            return "{0:.4f}".format(-curr[0])
        for index, weight in neighbors.items():
            new_neighbor = (-weight * curr[0], index)
            pq.put(new_neighbor)
            visited.add(new_neighbor)
    return 


def main():
    
    while True:
        dim = input().split()
        n = int(dim[0])
        m = int(dim[1])

        if n == 0 and m == 0:
            break
        adj = {}
        for i in range(m):
            input_row = input().split()
            index = int(input_row[0])
            vertex = int(input_row[1])
            weight = float(input_row[2])

            if index in adj:
                adj[index].update({vertex : -weight})
            else:
                adj[index] = {vertex : -weight}

        print(find_path_pq(adj, len(adj)))

if __name__ == "__main__":
    main()