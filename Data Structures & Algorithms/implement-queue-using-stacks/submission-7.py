class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        print(self.stack1, self.stack2)
        if not self.stack1:
            return -1
        for _ in range(len(self.stack1)-1):
            self.stack2.append(self.stack1.pop())
        self.stack2.reverse()
        self.stack1, self.stack2 = self.stack2, self.stack1
        return self.stack2.pop()

    def peek(self) -> int:
        if not self.stack1:
            return -1
        return self.stack1[0]

    def empty(self) -> bool:
        return not self.stack1


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()