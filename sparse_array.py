# https://www.hackerrank.com/challenges/sparse-arrays/problem

# Complete the matchingStrings function below.
def matchingStrings(strings, queries):
    ret = [0] * len(queries)
    counts = {}

    for item in strings:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1 

    for i in range(len(queries)):
        if queries[i] in counts:
            ret[i] = counts[queries[i]]
        else:
            ret[i] = 0
    return ret