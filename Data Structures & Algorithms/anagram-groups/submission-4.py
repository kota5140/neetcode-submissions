from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return []
        hashMap = defaultdict(list)
        for st in strs:
            count = [0]*26
            for c in st:
                count[ord(c)-97] += 1
            hashMap[tuple(count)].append(st)
        return list(hashMap.values())