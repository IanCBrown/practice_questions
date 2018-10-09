import sys

def ratios(string):
    length = len(string)
    whitespace_count = 0
    lower_count = 0
    upper_count = 0
    symbol_count = 0
    for char in string:
        if ord(char) == 95:
            whitespace_count += 1
        elif ord(char) >= 65 and ord(char) <= 90:
            upper_count += 1
        elif ord(char) >= 97 and ord(char) <= 122:
            lower_count += 1
        else:
            symbol_count += 1

    print(float(whitespace_count / length))
    print(float(lower_count / length))
    print(float(upper_count / length))
    print(float(symbol_count / length))



if __name__ == "__main__": 
    string_in = sys.stdin.readline()
    string_in.strip()
    ratios(string_in)