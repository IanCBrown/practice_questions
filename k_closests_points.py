import math

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        origin = (0,0)
        points.sort(key = lambda point: euclidean_distance(origin, point))
        return points[:K]
            
    
    
def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2) 