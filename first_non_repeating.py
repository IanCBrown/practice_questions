
def first_non_repeating_char(string):
    char_map = {}

    for s in string:
        if s in char_map:
            char_map[s] += 1
        else:
            char_map[s] = 1
    
    for key, value in char_map.items():
        if value == 1:
            return key
    return 



def nsquared(string):
    char_map = {}
    for s in string:
        if s not in char_map:
            char_map[s] = string.index(s)

    for key, value in char_map.items():
        if string.count(key) == 1:
            return key




test1 = "aaabcccdeeef"
test2 = "abcbad"
test3 = "abcabcabc"
test4 = "abbcbba"

print(nsquared(test1))
print(nsquared(test2))
print(nsquared(test3))
print(nsquared(test4))

print(first_non_repeating_char(test1))
print(first_non_repeating_char(test2))
print(first_non_repeating_char(test3))
print(first_non_repeating_char(test4))