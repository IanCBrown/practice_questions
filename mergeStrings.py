def  mergeStrings(a, b):
    a_len = len(a)
    b_len = len(b)
    ret = []

    shortest = min(a_len, b_len)
    longest = max(a_len, b_len)

    for i in range(shortest):
        ret.append(a[i])
        ret.append(b[i]) 
    for i in range(shortest, longest):
        if a_len == longest:
            ret.append(a[i])
        else:
            ret.append(b[i])
    return ''.join(ret)
    