class MinStack:
    def __init__(self):
        self.stack = []
        self.mini = []
    def push(self, val):
        self.stack.append(val)
        if val <= min(val, self.mini[-1] if self.mini else val):
            self.mini.append(val)
    def pop(self):
        val = self.stack.pop()
        if val == self.mini[-1]:
            self.mini.pop()
    def top(self):
        return self.stack[-1]
    def getMin(self):
        return self.mini[-1]











































''''class MinStack:

    def __init__(self):
        self.stack = []
        self.mini = []

    def push(self, val: int) -> None:
        if not self.mini:
            self.mini.append(val)
        else:
            self.mini.append(min(self.mini[-1], val))
        self.stack.append(val)
        

    def pop(self) -> None:
        self.stack.pop()
        self.mini.pop()
        

    def top(self) -> int:
        if not self.stack:
            return
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.mini[-1]'''

        
