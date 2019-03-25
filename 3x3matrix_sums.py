def matrix_sums():
    col_sum = [] 
    row_sum = [] 
    diag_sum = [] 

    # columns 1, 2, and 3 respectively 
    col_sum.append(s[0][0] + s[1][0] + s[2][0])
    col_sum.append(s[0][1] + s[1][1] + s[2][1])
    col_sum.append(s[0][2] + s[1][2] + s[2][2])

    # rows 1, 2, and 3 respectively 
    row_sum.append(s[0][0] + s[0][1] + s[0][2])
    row_sum.append(s[1][0] + s[1][1] + s[1][2])
    row_sum.append(s[2][0] + s[2][1] + s[2][2])

    # diag 1 and 2 respectively 
    diag_sum.append(s[0][0] + s[1][1] + s[2][2])
    diag_sum.append(s[0][2] + s[1][1] + s[2][0])

    col_mean = math.ceil(sum(col_sum) / len(col_sum))
    row_mean = math.ceil(sum(row_sum) / len(row_sum))
    diag_mean = math.ceil(sum(diag_sum) / len(diag_sum))

    print(col_sum)
    print(col_mean)
    print(row_sum)
    print(row_mean)
    print(diag_sum)
    print(diag_mean)
