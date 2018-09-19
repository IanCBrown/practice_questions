#!/usr/bin/env python


interval = int(input())

for i in range(0, interval):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz") 
    else:
        print(i)
