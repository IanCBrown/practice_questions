

def missing_numbers(sequence):
    curr = 1
    missing = []
    for i in range(sequence[-1]):
        if curr in sequence:
            curr += 1
            continue
        else:
            missing.append(curr)   
            curr += 1
    return missing

num_cases = int(input())
seq = []
while num_cases > 0:
    seq.append(int(input()))
    num_cases -= 1

ret = missing_numbers(seq)
if len(ret) == 0:
    print("good job")
else:
    print(*ret, sep="\n")