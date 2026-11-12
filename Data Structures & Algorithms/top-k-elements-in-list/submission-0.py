class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for _ in range(len(nums)+1)]
        for num in nums:
            count[num] = count.get(num, 0) + 1
        for num, cnt in count.items():
            freq[cnt].append(num)
        
        ans = []
        for i in reversed(range(len(freq))):
            if k == 0:
                return ans
            if len(freq[i]) == 0:
                continue
            for item in freq[i]:
                ans.append(item)
            k -= 1
            