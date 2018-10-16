
# Cracking the Coding Interview Problem 1.1 

def check_unique(string):
    # use a set to check that the param string only contains unique characters 
    visited = set()
    for char in string:
        visited.add(char)
    
    if len(visited) == len(string):
        return True
    else:
        return False 


def main(): 
    str_in = input("Input a string to check for all unique characters:\n")

    print(check_unique(str_in))


if __name__ == "__main__":
    main()