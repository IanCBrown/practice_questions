import sys


def shortest_rep(bus_list):
    bus_list.sort()    
    saved = [
        [bus_list[0]]
    ]
    num_collections = 0
    for i in range(1, len(bus_list)):
        if bus_list[i] - 1 == bus_list[i - 1]:
            saved[num_collections].append(bus_list[i])
        else:
            saved.append([bus_list[i]])
            num_collections += 1
   
    ret_string = ""
    for i in saved:
        if len(i) > 2:
            ret_string += str(i[0]) + "-" + str(i[-1]) + " "            
        elif len(i) == 2:
            ret_string += str(i[0]) + " " + str(i[1]) + " "
        else:
            ret_string += str(i[0]) + " "
    return ret_string



if __name__ == "__main__":
    num_of_buses = sys.stdin.readline()
    bus_numbers = sys.stdin.readline().split()
    bus_numbers = [int(x) for x in bus_numbers]
    print(shortest_rep(bus_numbers))



