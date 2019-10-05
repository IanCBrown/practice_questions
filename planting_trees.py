from queue import PriorityQueue


def planting_trees_list(seed_list):
    # [4,3,3,2]
    seed_list.sort(reverse=True)
    day = 1
    max_days = 0
    
    for seed in seed_list:
        if seed + day > max_days:
            max_days = seed + day
        day += 1

    return max_days + 1



num_trees = int(input())
trees = [int(x) for x in input().split()]
print(planting_trees_list(trees))