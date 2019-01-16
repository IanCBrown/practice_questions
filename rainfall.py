
def rainfall(city):
    total_water = 0 

    for i in range(len(city)):
        try:
            left_max = max(city[:i])
            right_max = max(city[i:])
            water_level = min(left_max, right_max)
            # subtract current building height
            temp = water_level - city[i]
            # print(str(i) + " " + str(temp))
            total_water += temp
        except ValueError:
            # i = 0 will produce a value error 
            # only evaluate right side in that case
            right_max = max(city[i:])
            temp = right_max - city[i]
            total_water += temp
            continue
    return total_water 



def main():
    test_city = [1,0,2,1,0,1,3,2,1,2,1]

    print(rainfall(test_city)) 





if __name__ == "__main__":
    main()