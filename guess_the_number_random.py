import sys
import random


if __name__ == "__main__":
    target = random.randint(0, 1000)
    print(target)
    low = 0 
    high = 1000
    steps = 0
    
    while target >= low and target <= high:
        guess = (low + high) // 2
        if guess == target:
            print("Found target " + str(target) + " in " + str(steps) + " steps.")
            break
        elif guess > target:
            high = guess
            steps += 1
        else:
            low = guess
            steps += 1
        
