import sys
import collections

# rushed implementation
# optimize later 
# https://open.kattis.com/problems/zoo
def unbearable(zoo_number, zoo):
    animal_set = set()
    counts = {}
    for animal in zoo:
        animal_set.add(animal)

    for animal in animal_set:
        counts[animal] = zoo.count(animal)

    counts = collections.OrderedDict(sorted(counts.items()))
    print("List %d:" % zoo_number)
    for k,v in counts.items():
        print(k + " | " + str(v))


def main():
    num = int(input())
    z_list = []
    zoo_number = 1 
    while num > 0:
        temp = sys.stdin.readline().split()
        z_list.append(temp[-1].lower())
        num -= 1
        if num == 0:
            unbearable(zoo_number, z_list)
            z_list = [] 
            zoo_number += 1
            num = int(input())
            continue
    


if __name__ == "__main__":
    main()