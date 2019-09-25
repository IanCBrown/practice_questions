import sys

class Node:
    def __init__(self, data):
        self.data = data
        self.parent = None


path = []
def solve(current_node):
    if current_node.parent is None:
        path.append(current_node.data)
        return  
    else:
        path.append(current_node.data) 
        solve(current_node.parent)

def helper(start, tree):
    relation = {}
    for branch in tree:
        relation[branch[0]] = [x for x in branch[1:]]
    return relation

def solution(start, relation):    
    if start not in relation:
        return 
    else:
        path.append(start)
        solution(get_parent(start, relation), relation)

def get_parent(curr, relation):
    for key, value in relation.items():
        if curr in value:
            return key
     

def main():
    # l = [int(x.strip()) for i in sys.stdin.readlines() for x in i]
    start = input()

    tree = []
    n = ""
    while n != ["-1"]:
        n = input().split()
        if n != ["-1"]:
            l = [i for i in n]
            tree.append(l)
        


    solution(start, helper(start, tree))
    print(*path, sep=' ')


if __name__ == "__main__":
    main()