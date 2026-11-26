class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n =  len(temperatures)
        res = [0] * n
        for i in range(n):
            if not stack or temperatures[i] <= temperatures[stack[-1]]:
                stack.append(i)
            else:
                while stack and temperatures[i] > temperatures[stack[-1]]:
                    prev_temp = stack.pop()
                    res[prev_temp] = i - prev_temp
                stack.append(i)
        return res