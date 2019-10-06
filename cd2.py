import sys

while True:
    case = sys.stdin.readline().split()
    n = int(case[0])
    m = int(case[1])

    if n == 0 and m == 0:
        break
    jack_list = []
    diff = 0
    for i in range(n):
        jack_list.append(sys.stdin.readline())
    for i in range(m):
        k = sys.stdin.readline()
        if k in jack_list:
            diff += 1 
    print(diff)
