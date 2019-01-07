
class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, data):
        self.stack.append(data)
    
    def pop(self):
        return self.stack.pop()

    def is_empty(self):
        return len(self.stack) > 0
    
    def print(self):
        print(self.stack)



if __name__ == '__main__':
    s = Stack()
    s.push(3)
    s.push(2)
    s.push(1)
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.is_empty())
    
