import sys

# original problem 
# https://open.kattis.com/problems/convexpolygonarea


num_of_polygons = 0

# convex polygon area 
def polygon_area(Xs, Ys, num_verticies):
    num_verticies = int(num_verticies)
    area = 0.0 

    # start at the end and increment forwards for shoelace method 
    j = num_verticies - 1
    for i in range(0, num_verticies):
        area += (Xs[j] + Xs[i]) * (Ys[j] - Ys[i]) 
        j = i
    return float(abs(area / 2))


def main():
    num_of_polygons = int(input())
    list_of_polys = []
    for i in range(num_of_polygons):
        list_of_polys.append([int(i) for i in input().split()])
    
    points = []
    
    for poly in list_of_polys:
        Xs = []
        Ys = []
        num_verticies = poly.pop(0)
        for i in range(0, len(poly), 2):
            Xs.append(poly[i])
        for j in range(1, len(poly), 2):
            Ys.append(poly[j])
        print(polygon_area(Xs, Ys, num_verticies))



if __name__ == "__main__":
    main()
    

# area = cross product * 1/2 