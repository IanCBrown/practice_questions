

while True:
    case = input().split()
    n = int(case[0])
    m = int(case[1])

    if n == 0 and m == 0:
        break
    jack_list = []
    jill_list = []
    for i in range(n):
        jack_list.append(int(input()))
    for i in range(m):
        jill_list.append(int(input()))
    
    combined = jack_list + jill_list
    s = set(combined)
    print(len(combined) - len(s))
