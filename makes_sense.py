import sys 

def main(): 
    num = int(input())
    line = sys.stdin.readline().split()
    print(line)
    
    mumble_count = 0 
    
    prev_num = 0 
    expected_num = 1 

    curr = 0 
    for i in range(len(line)):
        curr = line[i]
        if curr.isdigit() and expected_num == i:
            prev_num = int(curr)
            expected_num = int(curr) + 1
            mumble_count = 0 
        else: 
            # print("expected " + str(expected_num))
            # print("prev " + str(prev_num))
            mumble_count += 1
            # print("expected - prev " +  str(expected_num - prev_num))
            if expected_num > num:
                expected_num += 1
        print("curr " + str(curr))
        print("exp " + str(expected_num))
        # if curr != expected_num:
        #     print("something is fishy")
        #     return
    
    if mumble_count == num:
        print("makes sense")
    
            
    



if __name__ == "__main__":
    main()




   
    #         if expected_num - prev_num == mumble_count:
    #             continue
    #         elif mumble_count <= len(line): 
    #             if mumble_count == len(line):
    #                 print("makes sense")
    #                 return
    #         else:
    #             print("something is fishy")
    #             return