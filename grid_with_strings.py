import sys
from collections import deque

grid = []

def bfs(grid, n, m):
    visited = []
    q = [(0,0)]

    while q:
        node = q.pop(0)
        if node[0] == n and node[1] == m:
            visited.append(node)
            return visited
        if node not in visited:
            visited.append(node)
            neighbors = get_neighbors(node[0], node[1], grid[node[0]][node[1]], n, m)
            for neighbor in neighbors:
                q.append(neighbor) 


def solution(grid, n, m):
    visited = []
    start = (0,0)
    queue = deque([[start]])
    while queue:
        path = list(queue.popleft())
        node = path[-1]
        if node not in visited:
            neighbors = get_neighbors(node[0], node[1], grid[node[0]][node[1]], n, m)
            for neighbor in neighbors:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
                if neighbor[0] == n and neighbor[1] == m:
                    return new_path
            visited.append(node)
    return -1 
                

def get_neighbors(row, col, value, n, m):
    ret = [] 
    if row + int(value) <= n:
        ret.append((row + int(value), col))
    if row - int(value) >= 0:
        ret.append((row - int(value), col))
    if col + int(value) <= m:
        ret.append((row, col + int(value)))
    if col - int(value) >= 0:
        ret.append((row, col - int(value)))
    return ret


def main():
    dim = [int(x) for x in input().split()]
    n = dim[0]
    m = dim[1]

    grid = [list(line.strip()) for line in sys.stdin.readlines()]

    path = solution(grid, n - 1, m - 1)

    if path == -1:
        print(-1)
    else:
        print(len(path) - 1)


if __name__ == "__main__":
    main()