import sys
import collections

# rushed implementation
# optimize later 
# https://open.kattis.com/problems/zoo

def main():
    num = int(input())
    zoo = {}
    zoo_count = 1 

    while num != 0:
        temp = input().split()
        animal = temp[-1].lower()
        if animal in zoo:
            zoo[animal] += 1
        else:
            zoo[animal] = 1
        
        num -= 1
        if num == 0:
            # end of zoo 
            print("List %d:" % zoo_count)
            for animal, count in sorted(zoo.items()):
                print(animal + " | " + str(count))
            zoo = {}
            zoo_count += 1
            num = int(input())
            continue
    


if __name__ == "__main__":
    main()