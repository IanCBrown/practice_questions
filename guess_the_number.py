import sys

if __name__ == "__main__":
    low = 1 
    high = 1001
    while True:
        guess = (low + high) // 2
        print(str(guess))
        sys.stdout.flush()
        response = sys.stdin.readline().strip()
        if response.lower() == "correct":
            break
        elif response.lower() == "higher":
            low = guess
        else:
            high = guess 