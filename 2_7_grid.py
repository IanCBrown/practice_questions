from __future__ import absolute_import
import sys

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
    q = [[(0,0)]]

    while q:
        path = list(q.pop(0))
        node = path[-1]
        if node not in visited:
            neighbors = get_neighbors(node[0], node[1], grid[node[0]][node[1]], n, m)
            for neighbor in neighbors:
                new_path = list(path)
                new_path.append(neighbor)
                q.append(new_path)
                if neighbor[0] == n and neighbor[1] == m:
                    return new_path
            visited.append(node)
    return -1 
                

def get_neighbors(row, col, value, n, m):
    ret = [] 
    if row + value <= n:
        ret.append((row + value, col))
    if row - value >= 0:
        ret.append((row - value, col))
    if col + value <= m:
        ret.append((row, col + value))
    if col - value >= 0:
        ret.append((row, col - value))
    return ret


def main():
    dim = [int(x) for x in raw_input().split()]
    n = dim[0]
    m = dim[1]

    grid = [[int(x) for x in list(line.strip())] for line in sys.stdin.readlines()]

    path = solution(grid, n - 1, m - 1)

    if path == -1:
        print -1
    else:
        print len(path) - 1


if __name__ == u"__main__":
    main()