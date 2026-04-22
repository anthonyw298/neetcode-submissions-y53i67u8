class MinStack:

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
        return self.mini[-1]

        
