import sys
import fractions

def conversion(list):
    whole_nums = []
    remainders = []
    nums = []
    denom = 0
    numerator = 0
    length = len(list)
    for i in range(length):
        denom = list[i][0]
        numerator = list[i][1]
        whole_nums.append(denom // numerator)
        remainder = denom % numerator
        remainders.append(remainder)
        nums.append(numerator)
    for i in range(len(whole_nums)):
        print(str(whole_nums[i]) + " " + str(remainders[i]) + " " + '/' + " " +  str(nums[i]))


if __name__ == "__main__":
    list = [] 
    for i in sys.stdin:
        ab = i.split()
        ab[0] = int(ab[0])
        ab[1] = int(ab[1])
        list.append(ab)
    
    list.remove(list[-1])
    conversion(list)