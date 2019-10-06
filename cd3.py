import sys

while True:
    case = sys.stdin.readline().split()
    n = int(case[0])
    m = int(case[1])

    if n == 0 and m == 0:
        break

    info = [0] * (n + m)
    for i in range(n + m):
        info[i] = sys.stdin.readline()

    n_pointer = 0
    m_pointer = m
    count = 0
    while m_pointer < len(info):
        print(info[n_pointer] == info[m_pointer])
        if info[n_pointer] == info[m_pointer]:
            count += 1
        n_pointer += 1
        m_pointer += 1
    print(count)
