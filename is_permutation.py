# Cracking the Coding Interview 

def is_permutation(string_a, string_b):
    # check if string a is a permutation of string b
    for char in string_a:
        if char in string_b:
            continue
        else:
            return False
    return True




def main():
    perms = ["cat", "taco"]

    # expect true
    print(is_permutation(perms[0], perms[1]))

    # expect false
    print(is_permutation("charles", "leclerc"))


if __name__ == "__main__":
    main()