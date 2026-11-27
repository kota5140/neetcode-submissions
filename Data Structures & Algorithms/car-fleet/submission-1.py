class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        paired = sorted(zip(position, speed))
        sorted_position, sorted_speed = zip(*paired)
        for i in range(len(position)):
            while stack and sorted_speed[stack[-1]] > sorted_speed[i]:
                if (sorted_position[i] - sorted_position[stack[-1]]) / (sorted_speed[stack[-1]] - sorted_speed[i]) <= (target - sorted_position[i]) / sorted_speed[i]:
                    stack.pop()
                else:
                    break
            stack.append(i)
        return len(stack)