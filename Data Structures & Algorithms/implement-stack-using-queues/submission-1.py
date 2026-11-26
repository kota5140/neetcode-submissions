from collections import deque
class MyStack:

    def __init__(self):
        self.d1 = deque()
        self.d2 = deque()
        self.isOne = True

    def push(self, x: int) -> None:
        self.d1.append(x) if self.isOne else self.d2.append(x)

    def pop(self) -> int:
        if self.isOne:
            for _ in range(len(self.d1)-1):
                self.d2.append(self.d1.popleft())
            self.isOne = False
            return self.d1.popleft()
        else:
            for _ in range(len(self.d2)-1):
                self.d1.append(self.d2.popleft())
            self.isOne = True
            return self.d2.popleft()

    def top(self) -> int:
        return self.d1[-1] if self.isOne else self.d2[-1]

    def empty(self) -> bool:
        return (not self.d1) if self.isOne else (not self.d2)


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()