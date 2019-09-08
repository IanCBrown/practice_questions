
def count(input_str, char):
    counter = 0
    for ch in input_str:
        if ch == char:
            counter += 1
    return counter

def main():
    input_string = input("Enter a string: ")
    input_char = input("Enter a char to look for: ")

    print(count(input_str, input_char))


if __name__ == "__main__":
    main()
