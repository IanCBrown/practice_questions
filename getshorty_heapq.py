import heapq


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