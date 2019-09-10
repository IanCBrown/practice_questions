# Cracking the Coding Interview 

# too many returns 
def one_way(original, modified):
    if abs(len(original) - len(modified)) == 1:
        smaller = smaller_of_two_arrays(original, modified)
        larger = larger_of_two_arrays(original, modified)
        for char in smaller:
            if char not in larger:
                return False
        return True 
    else:
        diff_count = 0 
        for char in modified:
            if char not in original:
                diff_count += 1 
        if diff_count > 1:
            return False
        return True
    return False

def smaller_of_two_arrays(a, b):
    if len(a) < len(b):
        return a
    else:
        return b

def larger_of_two_arrays(a, b):
    if len(a) > len(b):
        return a
    else:
        return b


print(one_way("pale", "ple"))
print(one_way("pales", "pale"))
print(one_way("pale", "bale"))
print(one_way("pale", "bake"))