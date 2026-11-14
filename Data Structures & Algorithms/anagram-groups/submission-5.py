from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = defaultdict(list)
        for st in strs:
            array = [0]*26
            for c in st:
                array[ord(c)-97] += 1
            hashMap[tuple(array)].append(st)
        return list(hashMap.values())
        