class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        # if nothing is in the stack
        if not self.stack:
            self.stack.append((val, val))
        # if smth in the stack
        else: 
            current_min = min(val, self.stack[-1][1])
            self.stack.append((val, current_min))

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()

    def top(self) -> int:
        if self.stack: 
            return self.stack[-1][0]

    def getMin(self) -> int:
        if self.stack:
            return self.stack[-1][1]
