#!/usr/bin/env python

def lazy(string): 
    return ''.join(reversed(string))


def rev(string):
    string = list(string)
    j = len(string) - 1
    i = 0 

    while i < j:
        string[i], string[j] = string[j], string[i] 
        i+= 1
        j -= 1
    return ''.join(string)

def reverse_int(integer):
    integer = list(str(integer))
    j = len(integer) - 1
    i = 0 

    while i < j:
        integer[i], integer[j] = integer[j], integer[i] 
        i+= 1
        j -= 1
    return ''.join(integer)


print(rev("string"))
print(rev("gnirts"))
print(reverse_int(12345))

    