from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        n = len(nums)
        hashMap = defaultdict(int)
        array = [[] for _ in range(n+1)]
        for num in nums:
            hashMap[num] += 1
        for num in nums:
            if not num in array[hashMap[num]]:
                array[hashMap[num]].append(num)
        for li in reversed(array):
            for item in li:
                if len(li) > 0:
                    ans.append(item)
                    k -= 1
                if k == 0:
                    return ans

            