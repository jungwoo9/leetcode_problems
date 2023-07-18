class MinStack:

    def __init__(self):
        self.stack = []
        self.min_elem = None

    def push(self, val: int) -> None:
        if self.min_elem is None:
            self.min_elem = val
            self.stack += [val]
        elif val < self.min_elem:
            self.stack += [2*val - self.min_elem]
            self.min_elem = val
        else:
            self.stack += [val]
    
    def pop(self) -> None:
        if self.stack[-1] < self.min_elem:
            self.min_elem = 2 * self.min_elem - self.stack[-1]
            del self.stack[-1]
        else:
            del self.stack[-1]
            if self.stack == []:
                self.min_elem = None
            
    def top(self) -> int:
        if self.stack[-1] < self.min_elem:
            return self.min_elem
        
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_elem


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()