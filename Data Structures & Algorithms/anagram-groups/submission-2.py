class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return
        hashMap = {}
        ans = []
        counter = 0
        for st in strs:
            count = [0]*26
            for c in st:
                count[ord(c)-97] += 1
            if hashMap.get(str(count), float('-inf')) < 0:
                hashMap[str(count)] = counter
                ans.append([st])
                counter += 1
            else:
                ans[hashMap[str(count)]].append(st)
        return ans

