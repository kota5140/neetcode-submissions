class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        buf = []
        for i in range(len(prices)-1):
            buf.append(prices[i+1]-prices[i])
        for j in buf:
            if j > 0:
                ans += j
        return ans