import sys
import random

def main():
    line = input().split()
    num_of_rooms = int(line[0])
    num_of_booked_rooms = int(line[1])
    booked_rooms = [int(x) for x in sys.stdin.readlines()] 
    rooms = [i for i in range(1, num_of_rooms + 1)] 
    
    for i in booked_rooms:
        rooms.remove(i)
    
    print(rooms[random.randint(0,len(rooms) - 1)]) if len(rooms) > 0 else print("too late")
    

if __name__ == "__main__":
    main()