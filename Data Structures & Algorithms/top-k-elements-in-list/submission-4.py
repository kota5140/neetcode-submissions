from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        n = len(nums)
        hashMap = defaultdict(int)
        bucket = [[] for _ in range(n+1)]
        for num in nums:
            hashMap[num] += 1
        for key, value in hashMap.items():
            bucket[value].append(key)
        for freq in reversed(bucket):
            for item in freq:
                ans.append(item)
                k -= 1
                if k == 0:
                    return ans