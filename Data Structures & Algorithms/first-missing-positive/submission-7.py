class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        length = len(nums)
        i = 0
        while i < length:
            if nums[i] > 0 and nums[i] < length+1 and nums[i] != i+1 and nums[nums[i]-1] != nums[i]:
                buf = nums[i]
                nums[i] = nums[buf-1]
                nums[buf-1] = buf
                continue
            i += 1
        for i in range(length):
            if nums[i] != i+1:
                return i+1
        return length+1
        