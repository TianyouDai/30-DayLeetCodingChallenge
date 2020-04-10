class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minStack = []
        self.m = None

    def push(self, x: int) -> None:
        self.stack.append(x)
        if x < self.getMin():
            self.minStack.append(x)
        else:
            self.minStack.append(self.getMin())

    def pop(self) -> None:
        x = self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if len(self.stack) == 1:
            return self.stack[0]
        return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
