import sys
import math
# % = area of whole pizza - area of inside 
# area of whole pizza = pi * radius^2 
# area excluding crust = pi * (r - c) ^ 2

def cheese_percentage(radius, crust):
    total_area = math.pi * (radius ** 2)
    inner_area = math.pi * ((radius - crust) ** 2) 
    return (inner_area / total_area) * 100

if __name__ == "__main__":
    pizza = sys.stdin.readline().split()

    radius = int(pizza[0])
    crust = int(pizza[1])
    
    print(cheese_percentage(radius, crust))
    