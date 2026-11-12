class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashMap = {}
        for num in nums:
            if hashMap.get(num, 0) > 0:
                return True
            else:
                hashMap[num] = 1
        return False