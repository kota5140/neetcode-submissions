class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memory = {}
        for i, num in enumerate(nums):
            j = memory.get(target-num)
            if j != None:
                return [j, i]
            memory[num] = i