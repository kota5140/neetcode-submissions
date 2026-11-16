class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, suffix = [], []
        n = len(nums)
        prefix.append(1)
        suffix.append(1)
        for i in range(1, n):
            prefix.append(prefix[-1]*nums[i-1])
        for i in reversed(range(1, n)):
            suffix.append(suffix[-1]*nums[i])
        for i in range(n):
            prefix[i] = suffix[n-i-1] * prefix[i]
        return prefix