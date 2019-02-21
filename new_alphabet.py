import sys

key = {"a" : "@", 
    "b" : "8", 
    "c" : "(", 
    "d" : "|)", 
    "e" : "3", 
    "f" : "#", 
    "g" : "6", 
    "h" : "[-]", 
    "i" : "|", 
    "j" : "_|",
    "k" : "|<", 
    "l" : "1", 
    "m" : "[]\/[]",
    "n" : "[]\[]", 
    "o" : "0", 
    "p" : "|D",
    "q" : "(,)", 
    "r" : "|Z", 
    "s" : "$", 
    "t" : "']['", 
    "u" : "|_|", 
    "v" : "\/", 
    "w" : "\/\/", 
    "x" : "}{", 
    "y" : "`/", 
    "z" : "2"
    }

def main():
    line = sys.stdin.readline()
    line = line.lower()
    ret_string = []
    
    for char in line:
        if char in key:
            ret_string.append(key[char])
        else:
            ret_string.append(char)

    print(''.join(ret_string))


if __name__ == "__main__":
    main()