# Cracking the Coding Interview 

def compress(string):
    # solves the wrong problem
    # treat duplicates as unique 
    counts = {}
    for char in string:
        if char not in counts:
            counts[char] = list(string).count(char)
            
    ret = []
    for key, value in counts.items():
        ret.append(key + str(value))

    return "".join(ret)

def compress_slow(string):
    # slow but correct O(n^2) solution 
    ret = [] 
    i = 0
    while i < (len(string)):
        j = i + 1
        count = 1
        while j < len(string) and string[i] == string[j]:
            count += 1
            j += 1       
        ret.append(string[i] + str(count))
        i = j 
    return "".join(ret)


def compress_better(string):
    ret = [] 
    count_consecutive = 0 

    for i in range(len(string)):
        count_consecutive += 1

        if (i + 1 >= len(string) or string[i] != string[i + 1]):
            # ret.append(string[i].join([str(count_consecutive)]))
            ret.append(string[i] + str(count_consecutive))
            count_consecutive = 0 
    return "".join(ret)

print(compress("aabcccccaaa"))
print(compress_slow("aabcccccaaa"))
print(compress_better("aabcccccaaa"))