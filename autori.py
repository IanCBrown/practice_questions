# input: up to 100 length char string
# output: Short version of string containing each capital letter 
# strat: if character code is that of a capital letter, append it to output string. 
# if ord(char) is between 65 and 90 inclusive. 
import sys

for i in sys.stdin:
    i = i.strip("\n")
    ab = i.split("-")

ret_str = ""
for word in ab:
    if ord(word[0]) >= 65 and ord(word[0]) <= 90:
       ret_str = ret_str + word[0] 

print(ret_str)
