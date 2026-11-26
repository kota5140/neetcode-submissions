from collections import deque
class MyStack:

    def __init__(self):
        self.d1 = deque()
        self.d2 = deque()

    def push(self, x: int) -> None:
        self.d1.append(x)

    def pop(self) -> int:
        if not self.d1:
            return -1
        for _ in range(len(self.d1)-1):
            self.d2.append(self.d1.popleft())
        self.d1, self.d2 = self.d2, self.d1
        return self.d2.popleft()

    def top(self) -> int:
        if not self.d1:
            return -1
        return self.d1[-1]

    def empty(self) -> bool:
        return not self.d1


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()