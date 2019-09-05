

def trik(sequence):
    current_pos = 1
    
    for move in sequence:
        if move == "A" and current_pos == 1:
            current_pos = 2
        elif move == "A" and current_pos == 2:
            current_pos = 1
        elif move == "B" and current_pos == 2:
            current_pos = 3
        elif move == "B" and current_pos == 3:
            current_pos = 2
        elif move == "C" and current_pos == 1:
            current_pos = 3
        elif move == "C" and current_pos == 3:
            current_pos = 1
    return current_pos


def main():
    test = input()
    print(trik(test))


if __name__ == "__main__":
    main()
