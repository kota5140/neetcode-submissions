class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return []
        hashMap = {}
        for st in strs:
            count = [0]*26
            for c in st:
                count[ord(c)-97] += 1
            if hashMap.get(tuple(count), 0) == 0:
                hashMap[tuple(count)] = [st]
            else:
                hashMap[tuple(count)].append(st)
        return list(hashMap.values())

