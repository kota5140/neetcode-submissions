class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic_s = {}
        dic_t = {}
        for i in s:
            dic_s[i] = dic_s.get(i, 0) + 1
        for j in t:
            dic_t[j] = dic_t.get(j, 0) + 1
        if dic_s == dic_t:
            return True
        return False