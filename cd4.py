import sys

while True:
    case = sys.stdin.readline().split()
    n = int(case[0])
    m = int(case[1])

    if n == 0 and m == 0:
        break

    jack = set()
    for i in range(n):
        jack.add(sys.stdin.readline())

    jill = set()
    for i in range(m):
        jill.add(sys.stdin.readline())

    inter = jack.intersection(jill)

    print(len(inter))
