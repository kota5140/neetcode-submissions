class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        index = fast = 1
        n = len(nums)
        while fast < n:
            if nums[fast] != nums[index - 1]:
                nums[index] = nums[fast]
                index += 1
            fast += 1
        return index