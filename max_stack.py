class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.max_idx = 0


    def push(self, x: int) -> None:
        if len(self.stack) == 0:
            self.stack.append(x)
        else:
            if x >= max(self.stack):
                self.stack.append(x)
                self.max_idx = len(self.stack) - 1
            else:
                self.stack.append(x)

    def pop(self) -> int:
        if self.max_idx == len(self.stack) - 1:
            ret = self.stack.pop(-1)
            if len(self.stack) == 0:
                self.max_idx = 0
            else:
                self.max_idx = self.topMax()
        else:
            ret = self.stack.pop(-1)
        return ret

    def top(self) -> int:
        return self.stack[-1]

    def peekMax(self) -> int:
        return self.stack[self.max_idx]

    def popMax(self) -> int:
        ret = self.stack.pop(self.max_idx)
        if len(self.stack) == 0:
            self.max_idx = 0
        else:
            self.max_idx = self.topMax()
        return ret
    
    def topMax(self) -> int: #idx
        m = max(self.stack)
        
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i] == m:
                return i

# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
