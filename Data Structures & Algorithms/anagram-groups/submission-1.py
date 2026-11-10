class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            alpha = [0]*26
            for c in s:
                alpha[ord(c) - ord('a')] += 1
            d.setdefault(tuple(alpha), []).append(s)
        return list(d.values())