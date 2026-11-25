class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxValue = 0
        n = len(heights)
        left, right = 0, n-1
        while left < right:
            if min(heights[left], heights[right]) * (right - left) > maxValue:
                maxValue = min(heights[left], heights[right]) * (right - left)
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
        return maxValue