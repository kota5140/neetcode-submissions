class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        index1= index2 = 0
        isLeft = True
        ans = []
        while index1 < len(word1) or index2 < len(word2):
            if isLeft:
                if index1 < len(word1):
                    ans.append(word1[index1])
                    index1 += 1
                    isLeft = False
                else:
                    ans.append(word2[index2])
                    index2 += 1
            else:
                if index2 < len(word2):
                    ans.append(word2[index2])
                    index2 += 1
                    isLeft = True
                else:
                    ans.append(word1[index1])
                    index1 += 1
        return "".join(ans)

