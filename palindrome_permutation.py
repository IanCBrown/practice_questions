# Cracking the Coding Interview 

def palindrome_permutation(string):
    # remove spaces
    string = [i for i in string if i != " "]
    # if even length, all chars must have even count
    if len(string) % 2 == 0:
        for char in string:
            if string.count(char) % 2 != 0:
                return False
    # if odd length, only one char can have odd count
    else:
        odd_count = 0
        for char in string:
            if string.count(char) % 2 != 0: 
                odd_count += 1
            if odd_count > 1:
                return False
    return True

def palindrome_permutation_table(string):
    # remove spaces and send to lower case
    string = [i.lower() for i in string if i != " "]
    # using a table of ascii values 
    table = [i for i in range(ord("a"), ord("z"))]

    odd_count = 0

    for char in string:
        table[ord(char) - ord("a")] += 1 
        if table[ord(char) - ord("a")] % 2 == 0:
            odd_count -= 1
        else:
            odd_count += 1
    
    return odd_count <= 1


test_string = "tact coa"

#expect true 
print(palindrome_permutation(test_string))

print(palindrome_permutation_table(test_string))

