# input: up to 100 length char string
# output: Short version of string containing each capital letter 
# strat: if character code is that of a capital letter, append it to output string. 
# if ord(char) is between 65 and 90 inclusive. 
import sys

def autori_ascii(string):
       ret_str = ""
       for word in string:
              if ord(word[0]) >= 65 and ord(word[0]) <= 90:
                     ret_str = ret_str + word[0] 
       return ret_str

def main():
    input = sys.stdin.readline().split("-")
    print(autori_ascii(input))

if __name__ == "__main__":
    main()