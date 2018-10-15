
# original problem 
# https://open.kattis.com/problems/greedilyincreasing

def greedy(sequence):
    max = sequence[0]
    max_sequence = [] 
    max_sequence.append(max)
    for num in sequence:
        if num > max:
            max = num 
            max_sequence.append(num)
    return max_sequence


def main():
    length_of_sequence = int(input())
    sequence = input().split()
    sequence = [int(i) for i in sequence]
    greedy_sequence = greedy(sequence)

    print(len(greedy_sequence))
    print(*greedy_sequence)


if __name__ == "__main__":
    main()