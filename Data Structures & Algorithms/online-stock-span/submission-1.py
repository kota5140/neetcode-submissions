class StockSpanner:

    def __init__(self):
        self.stack = []
        self.span = [0] * 10000
        self.day = 0

    def next(self, price: int) -> int:
        curr_span = 1
        self.day += 1
        while self.stack and self.stack[-1][1] <= price:
            prev_day = self.stack.pop()[0]
            curr_span += self.span[prev_day]
        self.span[self.day] = curr_span
        self.stack.append([self.day, price])
        return curr_span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)