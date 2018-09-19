import sys

ab = 0
a = 0
b = 0
for i in sys.stdin:
    ab = i.split()
    a = int(ab[0])
    b = int(ab[1])

a = str(a)[::-1]
b = str(b)[::-1]
if a > b:
    print(a)
else:
    print(b)
