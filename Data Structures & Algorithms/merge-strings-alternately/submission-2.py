class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        index1 = index2 = 0
        l1 = len(word1)
        l2 = len(word2)
        ans = []
        while index1 < l1 or index2 < l2:
            if index1 < l1:
                ans.append(word1[index1])
                index1 += 1
            if index2 < l2:
                ans.append(word2[index2])
                index2 += 1
        return "".join(ans)

