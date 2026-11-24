class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        hashSet = set(nums)
        buf = []
        if not 1 in hashSet:
            return 1
        i = 0
        while True:
            if (1+i) in hashSet:
                i += 1
            else:
                return 1+i

        
        
        