class MyQueue:

    def __init__(self):
        self.stack = []
        self.start = self.end = -1

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.end += 1

    def pop(self) -> int:
        self.start += 1
        return self.stack[self.start]

    def peek(self) -> int:
        return self.stack[self.start+1]

    def empty(self) -> bool:
        return self.start == self.end


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()