import math

def main():
    vertices = input().split()
    vertices = [float(x) for x in vertices]
    # vertices 
    a = vertices[0]
    b = vertices[1]
    c = vertices[2]
    d = vertices[3]

    # semi_perimeter
    s = (a + b + c + d) / 2

    k = math.sqrt((s - a) * (s - b) * (s - c) * (s - d))

    print(k) 

    

if __name__ == "__main__":
    main()