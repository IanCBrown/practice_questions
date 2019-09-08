
def rainfall(city):
    total_water = 0 
    # this code must be out side the for loop b/c 
    # when i = 0, city[:0] returns an empty set. 
    # only evaluate right side when i = 0 
    right_max = max(city[0:])
    total_water += right_max - city[0]

    for i in range(1, len(city)):
        left_max = max(city[:i])
        right_max = max(city[i:])
        water_level = min(left_max, right_max)
        # subtract current building height
        temp = water_level - city[i]
        total_water += temp
        
    return total_water



def main():
    # correct answer: 6

    test_city = [1,0,2,1,0,1,3,2,1,2,1]

    print(rainfall(test_city))


 


if __name__ == "__main__":
    main()