class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            while True:
                if not stack or stack[-1] < 0 or asteroid > 0:
                    stack.append(asteroid)
                    break
                elif stack[-1] + asteroid == 0:
                    stack.pop()
                    break
                elif stack[-1] > abs(asteroid):
                    break
                else:
                    stack.pop()
        return stack
                
                