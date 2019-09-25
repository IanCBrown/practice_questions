

class Node:
    def __init__(self, data):
        self.data = data
        self.parent = None


def main():
    # l = [int(x.strip()) for i in sys.stdin.readlines() for x in i]

    ret = []

    Nodes = [Node] * 101 
    for i in range(101):
        Nodes[i] = Node(i)
    curr = Nodes[int(input())]
    ret.append(curr.data)
    while True:
        values = [int(x) for x in input().split()]
        parent = values[0]
        if parent == -1:
            break 

        for i in range(1, len(values)):
            Nodes[values[i]].parent = Nodes[parent]
    

    curr = curr.parent
    while curr is not None:
        ret.append(curr.data)
        curr = curr.parent

    print(*ret, sep=" ")


if __name__ == "__main__":
    main()