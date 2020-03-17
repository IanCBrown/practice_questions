class Vector2D:

    def __init__(self, v: List[List[int]]):
        self.vector = v
        self.flat = []
        self.flatten()
        self.idx = 0
        self.size = len(self.flat)

    def next(self) -> int:
        if self.hasNext():
            ret = self.flat[self.idx]
            self.idx += 1
            return ret

    def hasNext(self) -> bool:
        if self.idx >= 0 and self.idx < self.size:
            return True
        
    def flatten(self) -> List:
        self.flat = [i for j in self.vector for i in j]
        


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(v)
# param_1 = obj.next()
# param_2 = obj.hasNext()
