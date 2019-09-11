# Cracking the Coding Interview 

def compress(string):
    # solves the wrong problem
    # treat duplicates as unique 
    counts = {}
    for char in string:
        if char not in counts:
            counts[char] = list(string).count(char)

    ret = []
    for key, value in counts:
        ret.append(key + value)

    print(ret)

def compress_slow(string):
    # slow but correct O(n^2) solution 
    ret = [] 
    i = 0
    while i < (len(string) - 1):
        j = i + 1
        count = 1
        while string[i] == string[j] and j < len(string) - 1:
           count += 1
           j += 1         
        ret.append(string[i] + str(count))
        i = j 
    return "".join(ret)


# print(compress("aabcccccaaa"))
print(compress_slow("aabcccccaaa"))