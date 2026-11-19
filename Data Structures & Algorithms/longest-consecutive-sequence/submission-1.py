class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        hashSet = set(nums)
        buf = []
        for i in nums:
            if not i-1 in hashSet:
                buf.append(i)
        l = 0
        for j in range(len(buf)):
            le = 0
            while True:
                if buf[j]+1 in hashSet:
                    buf[j] += 1
                    le += 1
                else:
                    break
            if le > l:
                l = le
        return l+1