# convert string to its phonetic alphabet 
# HELLO - Hotel Echo Lima Lima Oscar 


alpha_map = {"A" : "ALPHA", "B":"BRAVO", "C" : "CHARLIE"}
def convert(string):
    ret = []
    string = string.upper()
    for i in range(len(string)):
        if string[i] in alpha_map:
            if i == len(string) - 1:
                ret.append(alpha_map[string[i]])
            else:
                ret.append(alpha_map[string[i]] + " ")
        else:
            ret.append(string[i])
    return "".join(ret)


print(convert("abc"))