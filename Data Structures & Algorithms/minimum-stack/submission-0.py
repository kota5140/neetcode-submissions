class MinStack:

    def __init__(self):
        self.store_stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.store_stack.append(val)
        local_min = val
        if self.min_stack:
            local_min = min(self.min_stack[-1], val)
        self.min_stack.append(local_min)

    def pop(self) -> None:
        self.store_stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.store_stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
        
