from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashMap = defaultdict(int)
        hashMap[0] = 1
        curr_sum = 0
        count = 0
        for num in nums:
            curr_sum += num
            count += hashMap[curr_sum-k]
            hashMap[curr_sum] += 1
        return count