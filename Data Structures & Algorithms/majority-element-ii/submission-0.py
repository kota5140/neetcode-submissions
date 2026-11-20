from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hashMap = defaultdict(int)
        n = len(nums)
        ans = []
        for num in nums:
            hashMap[num] += 1
            if hashMap[num] > (n // 3) and not num in ans:
                ans.append(num)
        return ans