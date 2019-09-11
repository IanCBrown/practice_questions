# Cracking the Coding Interview 
# Is every character in the string unique? 


def is_unique_set(string):
    ret_set = set()

    for char in string:
        ret_set.add(char)

    return len(ret_set) == len(string)


def is_unique_slow(string):
    # no extra data structures 
    for i in range(len(string)):
        for j in range(len(string)): 
            if i != j and string[i] == string[j]:
                return False
    
    return True

def is_unique_ascii(string):
    # no extra data structures 
    # sort by ascii code 

    l = list(string)
    l.sort()

    for i in range(len(l) - 1):
        if ord(l[i]) == ord(l[i + 1]):
            return False

    return True 



def main():
    test = "test string"
    # expect false
    print(is_unique_set(test))
    print(is_unique_slow(test))
    print(is_unique_ascii(test))

    # expect true
    test2 = "charles"
    print(is_unique_set(test2))
    print(is_unique_slow(test2))
    print(is_unique_ascii(test2))




if __name__ == "__main__":
    main()