# 	Repeats (A[1…n]: integer array)
# 1	count = 0
# 2	number = −∞
# 3	for i = 1…(n-1) do
# 4		if A[i]==A[i+1] then 
# 5			count=count+1
# 6			if number ≠ A[i] then
# 7				print number
# 8		number = A[i]
# 9	print count


def repeats(l):
    count = 0 
    number = None 
    for i in range(len(l) - 1):
        if l[i] == l[i + 1]:
            count += 1
            if number != l[i]:
                print(number)
        number = l[i]
    print("count: " + str(count))


def main():
    test1 = [1,2,3,3,3,4,5,6,6,7,8,8,8,8,1,2,3,3]
    test2 = [1,3,3,3,3,4]

    repeats(test1)
    repeats(test2)

if __name__ == '__main__':
    main()
