class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = []
        for i in range(len(min(strs, key=len))):
            for j in range(len(strs)-1):
                if strs[j][i] != strs[j+1][i]:
                    return "".join(ans)
            ans.append(strs[0][i])
        return "".join(ans)