import sys 

# original problem 
# https://open.kattis.com/problems/different


# takes in a list of pairs. (all integers)
def difference(list_of_pairs):
    return_string = ""
    for pair in list_of_pairs:
        return_string += str(abs(pair[0] - pair[1])) + "\n"
    return return_string


def main():
    list_of_pairs = []
    for i in sys.stdin:
        ab = i.split()
        list_of_pairs.append(ab)
    # nested list comprehension to convert each element of 2d array to int
    list_of_pairs = [[int(i) for i in pair] for pair in list_of_pairs]
    print(difference(list_of_pairs))

if __name__ == "__main__":
    main()
