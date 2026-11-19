class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        hashSet = set(nums)
        buf = []
        for i in hashSet:
            if not (i-1) in hashSet:
                buf.append(i)
        length = 1
        for j in range(len(buf)):
            current = 1
            while True:
                if buf[j]+1 in hashSet:
                    buf[j] += 1
                    current += 1
                else:
                    break
            if current > length:
                length = current
        return length